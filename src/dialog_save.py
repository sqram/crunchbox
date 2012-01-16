#!/usr/bin/env python
'''
This class handles the dialog box that pops up
when the user clicks save. It takes an instantiated
object of the Brunch class, so we can call a method
in Brunch when the user clicks 'ok'
'''

import gtk

class SaveDialog(gtk.Dialog):
	
	def __init__(self, brunch):
		gtk.Dialog.__init__(self,'Save Profile', brunch.layout.window, 0, None)
		
		self.profile_name = None
		# -- create widgets
		vbox = gtk.VBox()
		hbox = gtk.HBox()
		label1 = gtk.Label("profile name: ")
		entry = gtk.Entry()
		button = gtk.Button(' ok ')
		
		# -- arrange layout
		hbox.pack_start(label1, 0, 0, 0)
		hbox.pack_start(entry, 0, 0, 0)
		hbox.pack_start(button, 0, 0, 0)
		vbox.add(hbox)
		vbox.pack_start(gtk.HSeparator())
		self.action_area.pack_start(vbox)
		'''
		label2 = gtk.Label("Five seconds after you click 'ok', \
		\nthe program will take a screenshot of your screen. Use this \
		\ndelay to minimize any windows and pretify your desktop for \
		\nthe screen shot");
		vbox.pack_start(label2)
		'''
		name = entry.get_text()
		# -- event binding
		button.connect("button_press_event", self.ok_clicked, entry, brunch)
		self.show_all()
		
	def ok_clicked(self, e, data, entry, brunch):
		self.profile_name = entry.get_text()
		brunch.save_profile(self.profile_name)
		self.destroy()
