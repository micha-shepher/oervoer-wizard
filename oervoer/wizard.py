

import os
from oervoer import Oervoer
from delivery import Delivery
from globals import Globals
from gi.repository import Gtk, Pango
from printing import PrintingApp
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
        self.picklists = []
        self.letters = []
        self.testdir = testdir
        self.builder = builder
        self.kat100    = file('../data/briefkat100.txt','r').read()
        self.hond100   = file('../data/briefhond100.txt','r').read()
        self.katcombi  = file('../data/briefkatcombi.txt','r').read()
        self.hondcombi = file('../data/briefhondcombi.txt','r').read()
        self.katplus   = file('../data/briefkatplus.txt','r').read()
        self.hondplus  = file('../data/briefhondplus.txt','r').read()
        self.out = None
        for row in self.store:
            line ='geen resultaten voor {0},{1}'.format(row[1], row[2])
            self.picklists.append(line)
            self.letters.append(line)

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
        textview=self.builder.get_object('textview1')
        textview.set_buffer(self.buffer)
        self.next   = self.builder.get_object('button7')
        self.previous = self.builder.get_object('button6')
        self.first = self.builder.get_object('button9')
        self.position = 0
        self.type = 'Picklijst'
        for index, row in enumerate(self.store):
            if row[0]:
                dieren.append(row[2])
                order = self.find_order(index)
                if order:
                    result = self.oervoer.process_order(order) #TODO add factor!
                    if self.oervoer.no_vis[0]:
                        warning('Geen {0} voor {1} afzondering'.format(*self.oervoer.no_vis[1:]), self.window)
                        self.oervoer.no_vis = False, None, None
                    d = Delivery(self.testdir, order, result)
                    res = d.csvout()
                    print res
                    self.picklists[index] = res,order.get_owner(), order.get_animal()
                else:
                    self.picklists[index] = 'geen bestelling voor {0},{1}'.format(row[1], row[2]),'',''
        self.buffer.set_text(self.picklists[0][0])
        self.dialog.set_title('Picklijst voor {0},{1}'.format(*self.picklists[0][1:]))
        self.results = self.picklists
        response = self.dialog.run()
        
    def on_orders_row_changed(self, *args):
        pass
        
    def on_cursor_changed(self, tv):
        row = tv.get_cursor()[0]
        status = self.builder.get_object('statusbar1')
        vermijdstatus = self.builder.get_object('vermijdstatus')
        self.currentorder = self.find_order(row)
        donts = self.currentorder.get_donts()
        for st in status, vermijdstatus:
            st.pop(0)
            st.push(0, 'zonder {0}'.format(', '.join(donts)))

    def on_brieven( self, button ):
        dieren = []
        self.dialog = self.builder.get_object('dialog1')
        self.buffer = self.builder.get_object('briefresultaten')
        textview=self.builder.get_object('textview1')
        textview.set_buffer(self.buffer)
        self.next   = self.builder.get_object('button7')
        self.previous = self.builder.get_object('button6')
        self.first = self.builder.get_object('button9')
        self.position = 0
        self.type = 'Brief'
        for index, row in enumerate(self.store):
            if row[0]:
                dieren.append(row[2])
                order = self.find_order(index)
                if order:
                    result = order.get_result()
                    if not result:
                        self.letters[index] = 'bestelling voor {0},{1} nog niet uitgevoerd. Kies "picklijst" eerst.'.format(row[1], row[2])
                    else:
                        if   order.get_ras() == 'KAT' and order.get_kind() == '100':
                            self.brief = self.kat100
                        elif order.get_ras() == 'HOND' and order.get_kind() == '100':
                            self.brief = self.hond100
                        elif order.get_ras() == 'KAT' and order.get_kind() == 'COMBI':
                            self.brief = self.katcombi
                        elif order.get_ras() == 'HOND' and order.get_kind() == 'COMBI':
                            self.brief = self.hondcombi
                        elif order.get_ras() == 'KAT' and order.get_kind() == 'PLUS':
                            self.brief = self.katplus
                        else:
                            self.brief = self.hondplus
                        d = Delivery(self.testdir, order, result)
                        res = d.csvout(True)
                        print res
                        weight = float(row[6])*order.get_weight()
                        if order.get_ras() == 'KAT':
                            weight *= 35
                        else:
                            weight *= 25
                        brief = self.brief.format("{:%d %B %Y}".format(datetime.date.today()),
                                order.get_owner(),
                                order.get_kind(),
                                order.get_animal(), order.get_weight(), weight,
                                order.get_kind(), order.get_kind())
                        self.letters[index] = brief+res, order.get_owner(), order.get_animal()
                else:
                    self.letters[index] = 'geen bestelling voor {0},{1}'.format(row[1], row[2])
        self.buffer.set_text(self.letters[0][0])
        self.dialog.set_title("Brief voor {0},{1}".format(*self.letters[0][1:]))
        self.results = self.letters
        response = self.dialog.run()
        
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
            fv = float(value)
            self.store[path][6] = value
        except ValueError:
            warning( '%s is geen decimaal' % value, self.window)

    def on_include_clicked( self, *args ):
        self.vermijd = file('../data/smaak.dat').readlines() # temporary
        i, j, cursor = (0,0,0)
        path = self.builder.get_object('treeview1').get_cursor()
        index = path[0] if path else 0
        self.currentorder = self.find_order(index)
        donts = self.currentorder.get_donts()
        for row in self.vermijd:
            row = row.strip()
            if row.find('key') != -1:
                key = row.split(':')[1]
                print 'grid{0}'.format(key)
                grid = self.builder.get_object('grid{0}'.format(key))
                for btn in grid.get_children():
                    grid.remove(btn)
                i, j, cursor = (0,0,0)
            else:
                row = row.upper()
                button = Gtk.CheckButton(label=row, active=row in donts)
                #button.set_active(row in donts)
                grid.attach(button, i, j, 1, 1)
                cursor += 1
                i = cursor / 8
                j = cursor % 8

        self.dialogvermijd = self.builder.get_object('dialogvermijd')
        self.dialogvermijd.show_all()
        self.dialogvermijd.run()
        
    def on_vermijdsave_clicked(self, *args):
        buttons = []
        for i in ('vis', 'gevogelte', 'kleindier', 'grootdier', 'orgaan'):
            buttons.extend(self.builder.get_object('grid{0}'.format(i)).get_children())
        donts = [btn.get_label() for btn in buttons if btn.get_active()]
        self.currentorder.set_donts(donts)    
        self.dialogvermijd.hide()
        self.on_cursor_changed(self.builder.get_object('treeview1'))
        
    def on_vermijdcancel_clicked(self, *args):
        self.dialogvermijd.hide()
        
    def on_pakketgewicht_edited( self, *args ):
        print 'pakketgewicht edited'

    def on_quit_picklijst( self, *args ):
        self.dialog.hide()

    def on_first( self, *args ):
        self.position = 0
        self.buffer.set_text(self.results[0][0])
        self.dialog.set_title('{0} voor {1},{2}'.format(self.type,*self.results[0][1:]))
        self.first.set_sensitive(False)
        self.previous.set_sensitive(False)
        self.next.set_sensitive(True)
        
    def on_next( self, *args ):
        if self.position < len(self.results)-1:
            self.position += 1
            self.buffer.set_text(self.results[self.position][0])
            self.dialog.set_title('{0} voor {1},{2}',)
            self.previous.set_sensitive(True)
            self.first.set_sensitive(True)
        if self.position == len(self.results)-1:
            self.next.set_sensitive(False)
        self.dialog.set_title('{0} voor {1},{2}'.format(self.type,*self.results[self.position][1:]))
        
    def on_print_old( self, *args ):
        warning( 'printing results voor {0},{1}'.format(self.store[self.position][1],self.store[self.position][2]),
                self.window)        
        try:
            lpr =  subprocess.Popen("/usr/bin/lpr", stdin=subprocess.PIPE)
            lpr.stdin.write(self.results[self.position][0])
        except Exception as e:
            print e.message

    def on_print( self, *args ):
        warning( 'printing results voor {0},{1}'.format(self.store[self.position][1],self.store[self.position][2]),
                self.window)        
        file('/tmp/wizardprint','w').write(self.results[self.position][0])
        print_app = PrintingApp( '/tmp/wizardprint', self.window)

    def on_previous( self, *args ):
        if self.position > 0:
            self.position -= 1
            self.buffer.set_text(self.results[self.position][0])
            self.next.set_sensitive(True)
            self.first.set_sensitive(True)
        if self.position == 0:
            self.previous.set_sensitive(False)
        self.dialog.set_title('{0} voor {1},{2}'.format(self.type,*self.results[self.position][1:]))
        
    def on_quit_clicked( self, *args):
        orderfile = file('../test/orders.csv', 'w')
        orderfile.write(self.oervoer.orderhead)
        for order in self.oervoer.ordlist:
            orderfile.write(order.get_base()+','+','.join(order.get_donts())+'\n')
        orderfile.close()    
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
        textview.set_wrap_mode(Gtk.WrapMode.WORD)

    def load_store(self, store, testdir):
        
        self.oervoer = Oervoer(testdir+'products.csv',testdir+'orders.csv',testdir+'picklists.csv')
        self.oervoer.parse_products()
        self.ordlist = self.oervoer.parse_orders()
        store.clear()
        for order in self.ordlist:
            store.append([True, 
                          order.get_owner(), 
                          order.get_animal(), 
                          order.get_ras(), 
                          order.get_kind(), 
                          '{0}'.format(order.get_weight()), 
                          '1.0', 
                          '{0}'.format(order.get_package()), 
                          True])
    
    def about_activate(self, action):
        about_dlg = self.builder.get_object('aboutdialog1')
        about_dlg.run()
        about_dlg.hide()

    def quit_activate(self, action):
        Gtk.main_quit()


if __name__ == '__main__':
    builder = BuilderApp()
    Gtk.main()

