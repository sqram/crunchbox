from shutil import copyfile

class Conky:
	
	def __init__(self, base):
		self.base = base

	def save(self, profile_name):
		self.base.save(profile_name, 'conky')
		
	def load(self, profile_name):
		self.base.load(profile_name, 'conky')
		# conky restarts automatically when
		# .conkyrc is changed. all done here.
