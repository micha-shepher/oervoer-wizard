

import os

from gi.repository import Gtk

class Handlers:
    def __init__(self, store):
        self.store = store

    def on_saved( self, button ):
        print 'saving..'

    def ads( self, button ):
        print 'ads'

    def on_picklijst( self, button ):
        print 'picklijst'

    def on_connect( self, button ):
        print 'connect'

    def on_factor_clicked( self, *args ):
        print 'factor clicked'

    def on_uitvoeren_changed( self, widget, path ):
        self.store[path,0] = not self.store[path,0]
        print dir(widget)
        print 'include changed'

    def on_factor_changed( self, *args ):
        print 'factor changed'

    def on_include_clicked( self, *args ):
        print 'include changed'



class BuilderApp:
    def __init__(self):

        self.builder = Gtk.Builder()
        filename = 'oervoer.glade'

        self.builder.add_from_file(filename)
        store = self.builder.get_object('store')
        self.builder.connect_signals(Handlers(store))

        window = self.builder.get_object('window1')
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

