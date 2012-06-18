# This class handles i/o of files. Reading to and from config files
# happen here. And yes I know I shouldn't name this file and class 'io' as there's an io
# module in the standard lib...but i'll keep it this way unless i need to use that lib

import os
from shutil import copyfile
from subprocess import call
from os.path import basename
import plugins


class Io:

	def __init__(self, crunchbox):
		self.cb = crunchbox
		
		
	def save(self, profile_name, app_name, plugin_obj):
		# copy the current config to config-name. so for example,
		# .conkyrc would be copied into .conkyrc-profilename.
		# @profile_name = name of profile user entered in input box
		# @app_name = used to save the new cfg file in ~/,config/crunchbox/<app>/
		
		print '-'*30
				
		app_name = basename(app_name)
		if app_name[-1] == '.':
			app_name = app_name[:-1]

		print 'app name: ' + basename( app_name)

		for cfg in plugin_obj.cfg:
			src = cfg		
			dst = self.cb.cb_cfg_dir + '/%s/%s-%s' % (app_name, self.get_cfg_name(cfg), profile_name)
			copyfile(src, dst)
			print "Saving %s's current config into %s" % (src, dst)


		
				
		
	def load(self, profile_name, app_name, plugin_obj):
		'''opposite of save. copy config-name to .config'''
		app_name = basename(app_name)
		if app_name[-1] == '.':
			app_name = basename(app_name[:-1])
		print '-'*30
		print 'Loading app: ' + app_name
		print 'Profile name: ' +  profile_name

		# get content of config-name
		for cfg in plugin_obj.cfg:
			pn = self.get_cfg_name(cfg) + '-' + profile_name

			f = self.cb.cb_cfg_dir + '/%s/%s' % (app_name, pn)
			print "Loading cfg file: " + f
			c = open(f)
			content = c.read()
			c.close()

			# copy that content into original config in system
			c = open(cfg, 'w')
			c.write(content)
			c.close()
			print
		
	
	def delete_profile(self, widget, profile_name):
		# Profile name comes as whatever.jpg. Delete the extension
		profile_name = profile_name[:-4]
		
		# Store configs name to delete here
		to_delete = []

		for plugin in self.cb.plugin_objects:
			# Get original cfg name. ie, .conkyrc. Just split the original cfg path at the /
			# and take last list element.
			cfg_original = plugin.cfg.split('/')[-1]
			cfg_profile = '%s-%s' %  (cfg_original, profile_name)
			print cfg_profile	
			to_delete.append(cfg_profile)
			
		# Now we must visit every directory in ~/.config/crunchbox/configs
		# and delete the file. Remember, 'public' is a list of all file names
		# in the /plugins folder. And each file name has relevant dir in /crunchbox/configs
		# so if we have tint2.py in the /plugins dir, there will be a directory named titn2 in
		# crunchbox/configs/
		# (an alternative to this would be to traverse the whole /crunchbox/config/ dir, looking in 
		# every folder for the file we want to delete)
		
		for f in getattr(plugins, 'public'):
			dir_name = f[:-3] # remove .py from filenames.
			print dir_name
			#print "removing: " + self.cb.cb_cfg_dir + '/%s/%s' % (dir_name, cfg_profile)
			#os.remove(self.cb.cb_cfg_dir + '/%s/%s' % (dir_name, cfg_profile))
			#os.remove(self.cb.cb_cfg_dir + '/%s/%s' % (dir_name, cfg_profile))


	def get_cfg_name(self, path):
		# given the path to the config file, we extract the config file's name,
		# which is everything after the last /. so if path is ~/.conkyrc, we
		# return just .conkyrc
		l = path.split('/')
		return l[-1]
