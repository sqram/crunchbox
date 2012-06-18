#!/usr/bin/env python

import gtk

class SaveDialog(gtk.Dialog):
	
	def __init__(self, crunchbox):
		gtk.Dialog.__init__(self,'Save Profile', crunchbox.gui.window, 0, None)
		self.show()
		
		
		self.profile_name = None
		# -- create widgets
		label = gtk.Label("Profile Name: ")
		entry = gtk.Entry()
		entry.set_activates_default(gtk.TRUE)
		
		# -- arrange layout
		self.vbox.pack_start(label)
		self.vbox.pack_start(entry)
		
		self.add_button(gtk.STOCK_CANCEL, gtk.RESPONSE_CANCEL)
		self.add_button(gtk.STOCK_OK, gtk.RESPONSE_OK)

		self.set_default_response(gtk.RESPONSE_OK)
		# -- event binding
		#button.connect("button_press_event", self.ok_clicked, entry, crunchbox)
		self.show_all()
		response = self.run()

		if response == gtk.RESPONSE_OK:
			profile_name = entry.get_text()
			crunchbox.save_profile(profile_name)
			self.destroy()
		else:
			self.destroy()
		
	
