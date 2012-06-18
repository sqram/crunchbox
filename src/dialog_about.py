#!/usr/bin/env python
'''
This class handles the dialog box that pops up
when the user clicks save. It takes an instantiated
object of the Brunch class, so we can call a method
in Brunch when the user clicks 'ok'
'''

import gtk

class AboutDialog(gtk.AboutDialog):
	
	def __init__(self, brunch):
		gtk.AboutDialog.__init__(self)
		
		self.set_program_name("Crunchbox")

		self.set_website("http://none.io")
		self.set_copyright("by noneio")
		self.set_comments("A multiple themes switcher")
		self.set_license("Do as you wish :)\nTry to give some form of credit back if possible.")
		

		self.run()
		self.destroy()
		
	def test(self, w, e):
		print 'close me'
