from subprocess import call

class Nitrogen:
	
	def __init__(self, base):
		self.base = base

	def save(self, profile_name):
		self.base.save(profile_name, 'nitrogen')
		
	def load(self, profile_name):
		self.base.load(profile_name, 'nitrogen')
		
		# call --restore on nitrogen to load wallpaper
		call('nitrogen --restore &', shell=True)
