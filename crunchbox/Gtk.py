import gtk


class GTK:

	def __init__(self, base):
		self.base = base

	def save(self, profile_name):
		self.base.save(profile_name, 'gtk')
		
	def load(self, profile_name):
		self.base.load(profile_name, 'gtk')
			
		# refresh gtk
		e = gtk.gdk.Event(gtk.gdk.CLIENT_EVENT);
		e.send_event = True;
		e.message_type = gtk.gdk.atom_intern("_GTK_READ_RCFILES", False)
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
		



