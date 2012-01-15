from subprocess import call

class Openbox:

	def __init__(self, base):
		self.base = base

	def save(self, profile_name):
		self.base.save(profile_name, 'openbox')
		
	def load(self, profile_name):
		self.base.load(profile_name, 'openbox')

		# reload openbox's config
		call('openbox --reconfigure', shell=True)
