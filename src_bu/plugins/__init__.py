import os


public = []
for filename in os.listdir(os.path.dirname(__file__)):
	if not filename.startswith('.') and filename.endswith('.py') and not filename.startswith('__'):
		
		p = __import__('plugins.%s' % filename[:-3], fromlist=[])
		public.append(filename)


#mod = 'plugins.test'

#__import__(mod)
