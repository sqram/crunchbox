from subprocess import call
from os.path import expanduser

class Ncmpcpp:
	
	def __init__(self, io):
		self.io = io
		self.cfg = [
			expanduser("~/.ncmpcpp/config")
		]
		
		# This is the path to where crunchbox stores all this plugin's cfg
		self.class_name = self.__class__.__name__
		self.plugin_cfg_dir = expanduser('~/.config/crunchbox/configs/' + self.class_name)

	def save(self, profile_name, plugin_obj):
		self.io.save(profile_name, self.class_name, plugin_obj)

	def load(self, profile_name, plugin_obj):
		self.io.load(profile_name, self.class_name, plugin_obj)
	
		#TODO if ncmpcpp can apply new configs without restarting, do so here. 		

