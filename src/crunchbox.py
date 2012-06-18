#!/usr/bin/env python

import gtk
import os
from os.path import expanduser, join
from getpass import getuser
from subprocess import call
from dialog_save import SaveDialog
from dialog_about import AboutDialog
from  gui import Gui
from io import Io
import plugins
import gobject

#TODO - mpd, ncmpcpp, ob menu
class CrunchBox:

	def __init__(self):
		# Holds things like plugins.conky.Conky, plugins.tint2.Tint2, etc.
		# We can later make object out of them by adding ()
		# self.plugin_modules = [] 

		# This will hold instantiated objects of the plugin classes.
		# So if we have plugins.conky.Conky, this will hold a Conky obj.
		# This is needed when deleting profiles.
		self.plugin_objects = []

		# Where we will save our configs/dotfiles, screenshots, etc.
		self.cb_dir = expanduser('~/.config/crunchbox')
		self.cb_cfg_dir = self.cb_dir + '/configs/'
		self.cb_screenshots_dir = self.cb_dir + '/screenshots/'
		
		# Required startup method calls

		self.io = Io(self)
		self.load_plugins()
		self.cfg_dir_exists()
		self.check_plugins_cfg_dir()

		# instantiate objects and variables
		self.gui = Gui(self)	


	

	
	def cfg_dir_exists(self):
		# If ~/.config/crunchbox does not exist, user is running crunchbox for the first time.
		# So let's create our .config/crunchbox dir and inner dirs.
		if os.path.exists(self.cb_dir) == False:			
			os.mkdir(self.cb_dir)
			os.mkdir(self.cb_screenshots_dir)
			os.mkdir(self.cb_cfg_dir)



	def check_plugins_cfg_dir(self):
		# Each time the program is ran, we must check if for every plugin in src/plugins,
		# there's a matching folder in ~/.config/crunchbox/config/. So if the user made a new
		# plugin, say, src/plugins/irssi.py, crunchbox will make ~/.config/crunchbox/configs/Irssi,
		# where irssi's config file(s) will be saved. This is so it takes minimal effort to add support
		# for a new program. Just create <program>.py file and drop it in the plugins folder. Crunchbox
		# will take care of the rest.
		'''
		for filename in plugins.public:
			if os.path.exists(self.cb_cfg_dir + '/%s' % filename)  == False:
				# Put inside try, in case it already exists.
				print filename
				os.mkdir(self.cb_cfg_dir + '/%s' % filename) 
		'''
		for obj in self.plugin_objects:
			if os.path.exists(obj.plugin_cfg_dir) ==  False:
				os.mkdir(obj.plugin_cfg_dir)
	# load plugins
	def load_plugins(self):	
		# plugins.public is a list of filenames inside /plugins. (conky.py, bash.py, etc)
		# From those values, we can get the class name that belongs to each file. conky.py
		# would give us 'Conky'. To get the class name from each file, head over to the link:
		# stackoverflow.com/questions/452969/does-python-have-an-equivalent-to-java-class-forname
		# We instantiate an object from each class and store it in self.plugins_object. So then
		# When we want to save/load everything, just cycle the list calling .save() or .load()
		# on each object!
		for f in getattr(plugins, 'public'):
			m = getattr(plugins, f[:-3])
			module = getattr(m, f[:-3].capitalize())
			obj = module(self.io) # ie, obj = plugins.conky.Conky(self.io)
			self.plugin_objects.append(obj)
			

	
	
	# Save and about buttons
	def save_clicked(self, w, e):
		dialog = SaveDialog(self)
		
	def about_clicked(self, w, e):
		dialog = AboutDialog(self)
		
		
		
	def save_profile(self, profile_name):
		for o in self.plugin_objects:
			print 'plugin: ', o
			# remember, p is something like plugins.conky.Conky
			o.save(profile_name, o)	# ie, Conky.save('dark scheme', <conky instance>)
			print
			print

		# Configs have been saved. Take a screenshot
		self.save_screenshot(profile_name)

	def load_profile(self, w, e):
		'''this is called from gui.py when screenshot is clicked'''
		# img_name is the name of the screenshot, aka name of our profile
		name = w.get_data('img_name')		
		for o in self.plugin_objects:
			o.load(name, o)


	# Save screenshot to disk.
	# Thanks to toothr, bob2, dash and lalaland1125 on freenode's #python for this :)
	def check_screenshot(self, cmd, name):
		if call(args=cmd, shell=True) == 0:

			self.gui.append_screenshot(name)
			self.gui.window.show_all()
			return False
		else:
			self.check_screenshot(cmd)
	

	def save_screenshot(self, name):
		'''
		unfortunatelly, imagick's screenshots won't show composite windows
		transparency like conky or transparent terminals. so we use scrot
		when i figure out how to do it, then we only need to call() once with
		import -window root -resize 200x175\! %s/%s.jpg;\
		convert is part of imagemagick. so user needs that installed. along with scrot"
		'''
		# When we take a screenshot of the desktop, we hide the crunchbang window.
		self.gui.window.hide_all()

		path = expanduser('~/.config/crunchbox/screenshots')	
		# TODO make it so we don't have to use shell=True
		scrot = """scrot  '%s.jpg' -e "mv '%s.jpg' '%s/%s.jpg'";""" % (name, name, path, name)
		convert = """convert -resize 200x125\! '%s/%s.jpg' '%s/%s.jpg'""" % (path, name, path, name)	
		command = scrot + convert
		
		
		gobject.timeout_add(390,self.check_screenshot, command, name)

		
		print "The disappearing and reappearing of the program that you just saw is normal."
		print "It's so that the Crunchbox window isn't included in the screenshot."

		self.gui.window.realize()
	
					                              	
		
    	

cb = CrunchBox()
gtk.main()
