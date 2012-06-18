from subprocess import call
from os.path import expanduser

class Tint2:
	
	def __init__(self, base):
		self.base = base
		self.cfg = [
			expanduser('~/.config/tint2/tint2rc')
		]
		
		# This is the path to where crunchbox stores all this plugin's cfg
		self.class_name = self.__class__.__name__
		self.plugin_cfg_dir = expanduser('~/.config/crunchbox/configs/' + self.class_name)

	def save(self, profile_name, plugin_obj):
		self.base.save(profile_name, self.class_name, plugin_obj)

	def load(self, profile_name, plugin_obj):
		self.base.load(profile_name, self.class_name, plugin_obj)


					
		# restart tint2
		call('killall tint2;tint2 &', shell=True)
