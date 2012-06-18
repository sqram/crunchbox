import gtk as g
from os.path import expanduser

class Gtk:

	def __init__(self, base):
		self.base = base
		self.cfg = [expanduser('~/.gtkrc-2.0')]
		
		# This is the path to where crunchbox stores all this plugin's cfg
		self.class_name = self.__class__.__name__
		self.plugin_cfg_dir = expanduser('~/.config/crunchbox/configs/' + self.class_name)


	def save(self, profile_name, plugin_obj):
		self.base.save(profile_name, self.class_name, plugin_obj)

	def load(self, profile_name, plugin_obj):
		self.base.load(profile_name, self.class_name, plugin_obj)

	
		# refresh gtk
		e = g.gdk.Event(g.gdk.CLIENT_EVENT);
		e.send_event = True;
		e.message_type = g.gdk.atom_intern("_GTK_READ_RCFILES", False)
		e.data_format = 8
		e.send_clientmessage_toall();
	
		"""
		def _get_theme_settings(self):
			'''gets GTK's theme settings (theme and icon theme for now)'''
			defaults = gtk.settings_get_default()	
			theme_name = defaults.get_property("gtk-theme-name")
			icon_theme_name = defaults.get_property("gtk-icon-theme-name")
			return (theme_name, icon_theme_name)
		"""
		



