from subprocess import call

class Tint2:
	
	def __init__(self, base):
		self.base = base

	def save(self, profile_name):
		self.base.save(profile_name, 'tint2')
		
	def load(self, profile_name):
		self.base.load(profile_name, 'tint2')
		
		# restart tint2
		call('killall tint2;tint2 &', shell=True)
