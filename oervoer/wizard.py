

import os
from oervoer import Oervoer
from delivery import Delivery
from globals import Globals
from gi.repository import Gtk, Pango
import subprocess
import datetime

def warning( warning, window ):
    dialog = Gtk.MessageDialog(message_type=Gtk.MessageType.INFO,
                               buttons=Gtk.ButtonsType.CLOSE,
                               text=warning)

    dialog.set_transient_for(window)
    response = dialog.run()
    dialog.destroy()

        
class Handlers:
    def __init__(self, store, window, builder, testdir='../test'):
        self.store = store
        self.window = window
        self.oervoer = None
        self.results = []
        self.testdir = testdir
        self.builder = builder
        self.brief = file('../data/brief.txt','r').read()
        self.out = None
        for row in self.store:
            self.results.append('geen resultaten voor {0},{1}'.format(row[1], row[2]))
            print self.results[-1]
    def apply_css(self):
        
        provider = Gtk.CssProvider()

        self.buffer.create_tag(tag_name="title")
        self.buffer.create_tag(tag_name="text")

        css = file('../data/buffer.css').read()

        self.apply_css(self.buffer, provider)
        Gtk.StyleContext.add_provider(self.buffer.get_style_context(),
                                      provider,
                                      Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)

        #if isinstance(widget, Gtk.Container):
        #    widget.forall(self.apply_css, provider)

    def on_saved( self, button ):
        warning('saving...', self.window)
        print 'saving..'

    def set_oervoer(self, oervoer):
        self.oervoer = oervoer
        
    def set_testdir(self, testdir):
        self.testdir = testdir
        
    def set_builder(self, builder):
        self.builder = builder
        
    def ads( self, button ):
        print 'ads'

    def find_order(self, index):
        for order in self.oervoer.ordlist:
            if self.store[index][1] == order.get_owner() and \
               self.store[index][2] == order.get_animal():
               return order
        return None
    
    def on_picklijst( self, button ):
        dieren = []
        self.dialog = self.builder.get_object('dialog1')
        self.buffer = self.builder.get_object('picklijstresultaten')
        self.next   = self.builder.get_object('button7')
        self.previous = self.builder.get_object('button6')
        self.first = self.builder.get_object('button9')
        self.position = 0
        for index, row in enumerate(self.store):
            if row[0]:
                dieren.append(row[2])
                order = self.find_order(index)
                if order:
                    result = self.oervoer.process_order(order) #TODO add factor!
                    d = Delivery(self.testdir, order, result)
                    res = d.csvout()
                    print res
                    self.results[index] = res
                else:
                    self.results[index] = 'geen bestelling voor {0},{1}'.format(row[1], row[2])
        self.buffer.set_text(self.results[0])
        response = self.dialog.run()
        
    def on_brieven( self, button ):
        dieren = []
        self.dialog = self.builder.get_object('dialog1')
        self.buffer = self.builder.get_object('picklijstresultaten')
        self.next   = self.builder.get_object('button7')
        self.previous = self.builder.get_object('button6')
        self.first = self.builder.get_object('button9')
        self.position = 0
        for index, row in enumerate(self.store):
            if row[0]:
                dieren.append(row[2])
                order = self.find_order(index)
                if order:
					#TODO: detect if order needs to be processed or not!
                    #result = self.oervoer.process_order(order) #TODO add factor!
                    result = order.get_result()
                    if not result:
                        self.results[index] = 'bestelling voor {0},{1} nog niet uitgevoerd. Kies "picklijst" eerst.'.format(row[1], row[2])
                    else:
                        d = Delivery(self.testdir, order, result)
                        res = d.csvout(True)
                        print res
                        if order.get_ras() == 'KAT':
                            weight = 35*2*float(row[6])*order.get_weight()
                        else:
                            weight = 25*2*float(row[6])*order.get_weight()
                        brief = self.brief.format("{:%d %M %Y}".format(datetime.date.today()),
                                  order.get_owner(),
                                  order.get_kind(),
                                order.get_animal(), order.get_weight(), weight,
                                order.get_kind(), order.get_kind())
                        self.results[index] = brief+res
                else:
                    self.results[index] = 'geen bestelling voor {0},{1}'.format(row[1], row[2])
        self.buffer.set_text(self.results[index])
        response = self.dialog.run()
        
    def on_connect( self, button ):
        warning('connecting to mysql server...', self.window)
        print 'connect'

    def on_factor_clicked( self, *args ):
        print 'factor cliscked'

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

    def on_quit_picklijst( self, *args ):
        self.dialog.hide()
        print 'quitting textview'

    def on_first( self, *args ):
        self.position = 0
        self.buffer.set_text(self.results[0])
        self.first.set_sensitive(False)
        self.previous.set_sensitive(False)
        self.next.set_sensitive(True)
        
    def on_next( self, *args ):
        if self.position < len(self.results)-1:
            self.position += 1
            self.buffer.set_text(self.results[self.position])
            self.previous.set_sensitive(True)
            self.first.set_sensitive(True)
        if self.position == len(self.results)-1:
            self.next.set_sensitive(False)
        
    def on_print( self, *args ):
        print 'printing results voor {0},{1}'.format(self.store[self.position][1],self.store[self.position][2])
        try:
            lpr =  subprocess.Popen("/usr/bin/lpr", stdin=subprocess.PIPE)
            lpr.stdin.write(self.results[self.position])
        except:
            pass

    def on_previous( self, *args ):
        if self.position > 0:
            self.position -= 1
            self.buffer.set_text(self.results[self.position])
            self.next.set_sensitive(True)
            self.first.set_sensitive(True)
        if self.position == 0:
            self.previous.set_sensitive(False)
        
    def on_quit_clicked( self, *args):
        Gtk.main_quit()


class BuilderApp:
    def __init__(self):

        testdir = os.getenv(Globals.TESTENV) 
        if not testdir:
            testdir = '../test/'
        self.builder = Gtk.Builder()
        filename = '../data/oervoer.glade'

        self.builder.add_from_file(filename)
        store = self.builder.get_object('orders')

        window = self.builder.get_object('window1')
        self.load_store( store, testdir )
        self.handlers = Handlers(store, window, self.builder)
        self.builder.connect_signals(self.handlers)
        self.handlers.set_oervoer(self.oervoer)
        self.handlers.set_testdir(testdir)
        window.connect('destroy', lambda x: Gtk.main_quit())
        try:
            window.set_icon_from_file('../data/logo7-1.png')
        except:
            pass
        window.show_all()
        textview=self.builder.get_object('textview1')
        textview.modify_font(Pango.FontDescription('Monospace 9'))

    def load_store(self, store, testdir):
        
        self.oervoer = Oervoer(testdir+'products.csv',testdir+'orders.csv',testdir+'picklists.csv')
        self.oervoer.parse_products()
        self.ordlist = self.oervoer.parse_orders()
        store.clear()
        for order in self.ordlist:
            store.append([True, order.get_owner(), order.get_animal(), order.get_ras(), order.get_kind(), 
                          order.get_weight(), 1.0, order.get_package(), True])
    
    def about_activate(self, action):
        about_dlg = self.builder.get_object('aboutdialog1')
        about_dlg.run()
        about_dlg.hide()

    def quit_activate(self, action):
        Gtk.main_quit()


if __name__ == '__main__':
    builder = BuilderApp()
    Gtk.main()

