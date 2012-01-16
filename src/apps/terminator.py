class Terminator:

	def __init__(self):
		config_path = '/home/lyrae/.config/terminator'
		config_file = 'config'
		'''
		terminator stores all profiles in the same file. so we must copy the
		1. user changes default and other profiles
		2. user saves settings in brunch
		3. brunch copy terminatorrc
		and later user wants to restore a certain 'default' profile
		copy contents of terminatorrc-profile into terminator rc
		'''
