# This class deals with the GUI aspect of the program.
# It creates widgets and lays them out, and also does
# event handling for the widgets.
# It takes as an argument an object which is an instantiated
# object of the class crunchbox.


import gtk
import os
from os.path import expanduser
CONFIG_PATH = expanduser("~/.config/crunchbox/")




class Gui:

	def __init__(self, crunchbox):
		self.crunchbox = crunchbox

		# -- our window
		self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
		self.window.set_border_width(10)
		self.window.set_default_size(677, 350)
		self.window.set_title("crunchbox")

		# -- create widgets
		self.vbox_main = gtk.VBox()
		img = gtk.Image()
		self.sw = gtk.ScrolledWindow()
		hbox_top_buttons = gtk.HBox()
		self.vbox_middle = gtk.VBox()
		button_save = gtk.Button(stock=gtk.STOCK_SAVE)
		button_about = gtk.Button(stock=gtk.STOCK_ABOUT)

		self.tooltip = gtk.Tooltips()

		# -- Widget properties
		self.sw.set_policy(gtk.POLICY_AUTOMATIC, gtk.POLICY_AUTOMATIC)

		# -- arrange layout
		hbox_top_buttons.pack_start(button_save)
		hbox_top_buttons.pack_start(button_about)
		self.vbox_main.pack_start(hbox_top_buttons,0 ,0, 0)
		self.sw.add_with_viewport(self.vbox_middle)
		self.vbox_main.pack_start(self.sw, 1, 1, 1)
		# -- call start up method(s)
		self.load_screenshots()

		self.window.add(self.vbox_main)

		# -- event binding
		self.window.connect('destroy', lambda x: gtk.main_quit())
		button_save.connect("button_press_event", crunchbox.save_clicked)
		button_about.connect("button_press_event", crunchbox.about_clicked)

		self.window.show_all()


	def append_screenshot(self, name):
		'''appends screenshot to list when profile is saved'''
		image = self._create_image(self.crunchbox.cb_screenshots_thumbs_dir, name + '.png')

		hbox = self.boxlist[-1]
		num_children =  len(hbox.get_children())
		if num_children in [0,3]:
			hbox = gtk.HBox()
			hbox.pack_start(image)
			self.vbox_middle.add(hbox)
			hbox.show()
			self.boxlist.append(hbox)
		else:
			hbox.pack_start(image)
			hbox.show()




	def _create_image(self, path, f):
		'''creates button with screenshot inside and return it'''
		image = gtk.Image()
		image.set_from_file(path + f)
		b = gtk.Button()
		b.add(image)
		# store the screenshot name in the button so when we click the button
		# to set a profile, we know the profile name(remove the '.jpg' from it)
		b.set_data('img_name', f[:-4])
		b.show()
		image.show()
		b.connect("button_press_event", self.resolve_button_click, f)
		# Set a tooltip for this button. (display profile name on hover)
		self.tooltip.set_tip(b, f[:-4])
		return b

	def resolve_button_click(self, w, e, name):
		# When the user clicks a screenshot (which is inside a button),
		# we check to see if it was a left-click or right-click. If it
		# was a left click, load the profile. If right, present menu
		if e.button == 3:
			self.rightclick_menu(e, name, w)
		else:
			self.crunchbox.load_profile(w, e)


	def load_screenshots(self):
		'''loads screenshots when program is opened'''
		# -- load our screenshots from the cfg directory
		# We want each row to hold 3 images. If an HBox has 3 children,
		# create a new HBox and append the upcoming image to it.

		# a list containing hboxes; start with one inside
		self.boxlist = [gtk.HBox()]
		screenshots = os.listdir(self.crunchbox.cb_screenshots_thumbs_dir)
		for f in screenshots:
			image = self._create_image(self.crunchbox.cb_screenshots_thumbs_dir, f)
			if len(self.boxlist[-1].get_children()) == 3:
				self.boxlist.append(gtk.HBox())

			self.boxlist[-1].pack_start(image)
		# sacrificing a for loop here for one liner neatness.
		map(lambda box: self.vbox_middle.pack_start(box,0,0,0), self.boxlist)

	def rightclick_menu(self, e, name, button):
		menu = gtk.Menu()
		item_delete = gtk.MenuItem('delete from crunchbox')
		menu.append(item_delete)
		menu.popup(None, None, None, e.button , e.time)
		menu.show_all()
		# we send the button widget because after we delete this profile, we remove it from the gui
		item_delete.connect('activate', self.crunchbox.io.delete_profile, name, button)



