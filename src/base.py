'''
This class serves as the base class for all classes in the 'crunchbox' dir.
Its purpose is to save & load configs.
'''
import os
from shutil import copyfile
from subprocess import call


class Base:

	def __init__(self, crunchbox):
		self.cb = crunchbox
		self.cfg_files = self.cb.cfg_files
		
		
	def save(self, profile_name, app_name):
		'''
		copy the current config to config-name. so for example,
		.conkyrc would be copied into .conkyrc-profilename.
		@profile_name = name of profile user entered in input box
		@app_name = used to save the new cfg file in ~/,config/crunchbox/<app>/
		'''
		src = self.cfg_files[app_name]

		dst_path = self.cb.cb_cfg_dir + '/crunchbox/%s' % app_name
		dst_file = self.get_cfg_name(self.cfg_files[app_name]) + '-' + profile_name
		
		dst_uri = os.path.join(dst_path, dst_file)
		copyfile(src, dst_uri)
		
		
	def load(self, profile_name, app_name):
		'''opposite of save. copy config-name to .config'''
		# get content of config-name
		pn = self.get_cfg_name(self.cfg_files[app_name]) + '-' + profile_name
		f = self.cb.cb_cfg_dir + '/crunchbox/%s/%s' % (app_name, pn)
		cfg = open(f)
		content = cfg.read()
		cfg.close()
		
		# copy that content into config
		print "opening %s" % self.cfg_files[app_name]
		cfg = open(self.cfg_files[app_name], 'w')
		cfg.write(content)
		cfg.close()
		
		
	def get_cfg_name(self, path):
		'''
		given the path to the config file, we extract the config file's name,
		which is everything after the last /. so if path is ~/.conkyrc, we
		return just .conkyrc
		'''
		l = path.split('/')
		return l[-1]
