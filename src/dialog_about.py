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

		self.set_website("http://kat.sh")
		#self.set_copyright("katsh")
		self.set_comments("A multiple themes switcher")
		self.set_license("GNU GENERAL PUBLIC LICENSE")
		self.set_authors(['katsh'])
		self.set_artists(['No one. Looking for someone to design a logo.'])


		self.run()
		self.destroy()

