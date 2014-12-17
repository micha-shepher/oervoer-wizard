

import os

from gi.repository import Gtk

def warning( warning, window ):
    dialog = Gtk.MessageDialog(message_type=Gtk.MessageType.INFO,
                               buttons=Gtk.ButtonsType.CLOSE,
                               text=warning)

    dialog.set_transient_for(window)
    response = dialog.run()
    dialog.destroy()

class Handlers:
    def __init__(self, store, window):
        self.store = store
        self.window = window

    def on_saved( self, button ):
        warning('saving...', self.window)
        print 'saving..'

    def ads( self, button ):
        print 'ads'

    def on_picklijst( self, button ):
        warning('picklijst...', self.window)
        print 'picklijst'

    def on_connect( self, button ):
        warning('connecting to mysql server...', self.window)
        print 'connect'

    def on_factor_clicked( self, *args ):
        print 'factor clicked'

    def on_uitvoeren_changed( self, widget, path ):
        self.store[path][0] = not self.store[path][0]
        print 'include changed'

    def on_factor_changed( self, widget, path, value ):
        try:
            self.store[path][6] = float(value)
        except ValueError:
            print '%s is not a floating point number' % value 
        print 'factor changed'

    def on_include_clicked( self, *args ):
        print 'include changed'

    def on_pakketgewicht_edited( self, *args ):
        print 'pakketgewicht edited'

    def on_quit_clicked( self, *args):
        Gtk.main_quit()


class BuilderApp:
    def __init__(self):

        self.builder = Gtk.Builder()
        filename = 'oervoer.glade'

        self.builder.add_from_file(filename)
        store = self.builder.get_object('orders')
        store.append([True,'Engelbert', 'Humperdinck', 'Hond', 'Combi', 25, 1.1, 20])
        self.load_store( store )

        window = self.builder.get_object('window1')
        self.builder.connect_signals(Handlers(store, window))
        window.connect('destroy', lambda x: Gtk.main_quit())
        window.show_all()

    def about_activate(self, action):
        about_dlg = self.builder.get_object('aboutdialog1')
        about_dlg.run()
        about_dlg.hide()

    def quit_activate(self, action):
        Gtk.main_quit()


if __name__ == '__main__':
    builder = BuilderApp()
    Gtk.main()

