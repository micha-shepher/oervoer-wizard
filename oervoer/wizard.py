

import os
from oervoer import Oervoer
from delivery import Delivery
from globals import Globals
from gi.repository import Gtk, Pango
from printing import PrintingApp
import subprocess
import datetime
import pickle

def warning( warning, window ):
    dialog = Gtk.MessageDialog(message_type=Gtk.MessageType.INFO,
                               buttons=Gtk.ButtonsType.CLOSE,
                               text=warning)

    dialog.set_transient_for(window)
    dialog.modify_font(Pango.FontDescription('Monospace 9'))
    response = dialog.run()
    dialog.destroy()

class Handlers:
    def __init__(self, store, window, builder, testdir='../test'):
        self.store = store
        self.window = window
        self.oervoer = None
        try:
            self.letters = pickle.load(file('../data/wizard.brief','r'))
            self.picklists = pickle.load(file('../data/wizard.pick','r'))
            # take care the pickled picklist array not too short!
            while len(self.store) > len(self.picklists):
                self.picklists.append((1,1,1))
            # take care the pickled letter array not too short!
            while len(self.store) > len(self.letters):
                self.letter.append((1,1,1))
        except IOError:
            self.picklists = []
            self.letters = []
            for row in self.store:
                line ='Geen resultaten voor {0},{1}'.format(row[1], row[2]), row[1], row[2]
                self.picklists.append(line)
                self.letters.append(line)
        self.results = []
        self.testdir = testdir
        self.builder = builder
        self.kat100    = file('../data/briefkat100.txt','r').read()
        self.hond100   = file('../data/briefhond100.txt','r').read()
        self.katcombi  = file('../data/briefkatcombi.txt','r').read()
        self.hondcombi = file('../data/briefhondcombi.txt','r').read()
        self.katplus   = file('../data/briefkatplus.txt','r').read()
        self.hondplus  = file('../data/briefhondplus.txt','r').read()
        self.vbutton   = builder.get_object('voorkeur_button')
        self.vbutton.set_sensitive(False)
        self.out = None
        self.portiestore = self.builder.get_object('portiestore')
        self.portiestore.clear()
        self.portiecombo = self.builder.get_object('portiecombostore')
        self.portiecombo.clear()
        for t in ('beide', 'kleine porties', 'grote porties'):
            self.portiecombo.append([t])

        self.donts_or_prefer = 'donts'

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
        warning('opslaan resultaten in tijdelijk bestand...', self.window)
        pickle.dump(self.picklists, file('../data/wizard.pick', 'w'))
        pickle.dump(self.letters,   file('../data/wizard.brief', 'w'))
        print 'opslaan in wizard.pick en wizard.brief'

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
        
        self.type = 'Picklijst'
        for index, row in enumerate(self.store):
            if row[0]:
                dieren.append(row[2])
                order = self.find_order(index)
                order.set_portie(row[9])
                if order:
                    result = self.oervoer.process_order(order) #mealsize adjusted by factor
                    for ex in self.oervoer.exceptions:
                        warning('Geen {0} voor {1} afzondering'.format(*ex), self.window)
                    self.oervoer.exceptions = []
                    d = Delivery(self.testdir, order, result)
                    res = '''datum: {7}\ndier: {0}\npakket: {1}\ngewicht dier: {2}\ngewicht pakket: {3}\nvermijd: {5}\nmaaltijd: {6}\n{4}'''.format(row[3],row[4],row[5], row[7], d.csvout(),
                                                                        ','.join(order.get_donts()),order.get_meal_size(),
                                                                        "{:%d %B %Y}".format(datetime.date.today() ))
                    print res
                    self.picklists[index] = res,order.get_owner(), order.get_animal()
                else:
                    self.picklists[index] = 'geen bestelling voor {0},{1}'.format(row[1], row[2]),'',''
        self.buffer.set_text(self.picklists[self.position][0])
        self.dialog.set_title('Picklijst voor {0},{1}'.format(*self.picklists[self.position][1:]))
        self.results = self.picklists
        response = self.dialog.run()
        
    def on_orders_row_changed(self, *args):
        pass
    
    def on_combo_edited(self, widget, path, text):
        print path, text
        self.store[path][9] = text
    
    def on_cursor_changed(self, tv):
        row = tv.get_cursor()[0]
        st = self.builder.get_object('statusbar1')
        self.currentorder = self.find_order(row)
        self.position = int(row.to_string())
        st.pop(0)
        if self.donts_or_prefer == 'donts':
            st.push(0, 'zonder: {0}'.format(', '.join(self.currentorder.get_donts())))
        else:
            st.push(0, 'houdt van: {0}'.format(', '.join(self.currentorder.get_prefers())))

    def on_brieven( self, button ):
        dieren = []
        self.dialog = self.builder.get_object('dialog1')
        self.buffer = self.builder.get_object('briefresultaten')
        textview=self.builder.get_object('textview1')
        textview.set_buffer(self.buffer)
        self.next   = self.builder.get_object('button7')
        self.previous = self.builder.get_object('button6')
        self.first = self.builder.get_object('button9')
        
        self.type = 'Brief'
        for index, row in enumerate(self.store):
            if row[0]:
                dieren.append(row[2])
                order = self.find_order(index)
                if order:
                    result = order.get_result()
                    if not result:
                        self.letters[index] = 'bestelling voor {0},{1} nog niet uitgevoerd. Kies "picklijst" eerst.'.format(row[1], row[2]),\
                                              order.get_owner(), order.get_animal()
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
                    self.letters[index] = 'Geen bestelling voor {0},{1}'.format(row[1], row[2]), order.get_owner(), order.get_animal()
            #else:
            #    self.letters[index] = 'Geen bestelling voor {0},{1}'.format(row[1], row[2]), order.get_owner(), order.get_animal()
        self.buffer.set_text(self.letters[self.position][0])
        self.dialog.set_title("Brief voor {0},{1}".format(*self.letters[self.position][1:]))
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
            self.currentorder.set_factor(fv)
        except ValueError:
            warning( '%s is geen decimaal' % value, self.window)

    def on_vermijd_clicked( self, *args ):
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

        self.donts_or_prefer = 'donts'
        st = self.builder.get_object('vermijdstatus')
        st.pop(0)
        st.push(0, 'zonder {0}'.format(', '.join(donts)))

        self.vbutton.set_sensitive(True)
        self.dialogvermijd = self.builder.get_object('dialogvermijd')
        self.dialogvermijd.set_title('Kies smaken te vermijden voor {0}'.format(self.currentorder.get_animal()))
        self.dialogvermijd.show_all()
        self.dialogvermijd.run()
        
    def on_portie_selected(self, selection):
        model, iter = selection.get_selected()
        vlees = model[iter][0] 
        tv = self.builder.get_object('treeview3')
        dialog = self.builder.get_object('dialog2')
        model = tv.get_model()
        prodlist = self.restrictlist[vlees]
        
        deleterange = range(len(prodlist), len(model))
        for i in deleterange:
            try:
                model.remove(model.get_iter(len(model)-1)) # pop the last one
            except:
                print '%%%%!!!!!!!!!!!!!!!', i, len(model), len(prodlist)
        
        for i, prod in enumerate(prodlist):
            if i < len(model):
                model[i][:] = (prod.name, str(int(prod.get_norm_weight()*1000)), str(prod.get_qty()), prod.smaak)
            else:
                model.append([prod.name, str(int(prod.get_norm_weight()*1000)), str(prod.get_qty()), prod.smaak])
        
        dialog.set_title('Geschikte producten in de categorie {} voor {}'.format(vlees,self.currentorder.get_animal()))
        dialog.show_all()
        dialog.run()
            
    def on_gezien_clicked(self, *arg):
        tv = self.builder.get_object('treeview3')
        dialog = self.builder.get_object('dialog2')
        dialog.hide() 
        
    def populate_portie(self, avan, atot, bvan, btot):
        store = self.builder.get_object('portiestore')
        #store.clear()
        self.restrictlist = {}
        for i, t in enumerate(Globals.VLEES_TYPES):
            num2 = 0
            num1 = len(self.oervoer.prodlists[t])
            self.restrictlist[t] = []
            if t in Globals.VLEES_DEELBAAR:
                van = avan/1000.0
                tot = atot/1000.0
            else:
                van = bvan/1000.0
                tot = btot/1000.0
            for prod in self.oervoer.prodlists[t]:
                if prod.get_norm_weight() >= van and\
                   prod.get_norm_weight() <= tot and\
                   not prod.smaak in self.currentorder.get_donts() and\
                   not prod.type  in self.currentorder.get_donts() and\
                   set(prod.smaak.split('.')).isdisjoint(set (self.currentorder.get_donts()) ) and\
                   prod.kathond[self.currentorder.ras]:
                    self.restrictlist[t].append(prod)
                    num2 += 1
            if len(store)<len(Globals.VLEES_TYPES):
                store.append([t,str(num1),str(num2),num2>0])
            else:
                store[i][1:] = (str(num1),str(num2),num2>0)
                #already in place
    
    def on_portie_quit(self, *arg):
        path = self.builder.get_object('treeview1').get_cursor()
        index = path[0] if path else 0
        
    def on_include_clicked(self, *arg):
        self.portie = self.builder.get_object('dialogportie')
        self.builder.get_object('entryras').set_text(self.currentorder.get_ras())
        self.builder.get_object('entrynaam').set_text(self.currentorder.get_animal())
        self.builder.get_object('entrygewicht').set_text(str(self.currentorder.get_weight()))
        factor = self.currentorder.get_factor()
        self.builder.get_object('entryfactor').set_text(str(factor))
        meal = self.currentorder.get_meal_size() * 1000
        self.builder.get_object('entrymaaltijd').set_text(str(meal))
        factvvan = meal * Globals.MEALFACTOR2
        factvtot = meal * Globals.MEALFACTOR
        factovan = round(meal / Globals.MEALFACTOR3) 
        factotot = meal * Globals.MEALFACTOR3

        self.builder.get_object('entryvvan').set_text(str(factvvan))
        self.builder.get_object('entryvtot').set_text(str(factvtot))
        self.builder.get_object('entryovan').set_text(str(factovan))
        self.builder.get_object('entryotot').set_text(str(factotot))
        self.builder.get_object('entryvermijd').set_text(','.join(self.currentorder.get_donts()))
        self.populate_portie(factvvan,factvtot,factovan,factotot)
        
        self.portie.show_all()
        self.portie.run()

    def on_entryfactor_activate(self, entryfactor, *args):
        try:
            factor = float(entryfactor.get_text())
        except ValueError:
            warning('{0} is geen acceptabele factor.'.format(entryfactor.get_text()), self.window)
            return
        if factor< 0.2 or factor > 5.0:
            warning('factor moet tussen 0.2 en 5 liggen.', self.window)
            return
        
        self.currentorder.set_factor(factor)
        self.store[self.position][6] = str(factor)
        meal = self.currentorder.get_meal_size() * 1000
        self.builder.get_object('entrymaaltijd').set_text(str(meal))
        avan = self.builder.get_object('entryvvan')
        atot = self.builder.get_object('entryvtot')
        bvan = self.builder.get_object('entryovan')
        btot = self.builder.get_object('entryotot')
        factvvan = meal * Globals.MEALFACTOR2
        factvtot = meal * Globals.MEALFACTOR
        factovan = round(meal / Globals.MEALFACTOR3) 
        factotot = meal * Globals.MEALFACTOR3
        avan.set_text(str(factvvan))
        atot.set_text(str(factvtot))
        bvan.set_text(str(factovan))
        btot.set_text(str(factotot))
        self.populate_portie(factvvan, 
                             factvtot, 
                             factovan, 
                             factotot)
        
    def on_portie_quit(self, *args):
        self.portie.hide()
                        
    def on_vermijdsave_clicked(self, *args):
        buttons = []
        for i in ('vis', 'gevogelte', 'kleindier', 'grootdier', 'orgaan', 'pensbot'):
            buttons.extend(self.builder.get_object('grid{0}'.format(i)).get_children())
        selections = [btn.get_label() for btn in buttons if btn.get_active()]
        if self.donts_or_prefer == 'prefer':
            self.currentorder.set_prefers(selections)    
        else:
            self.currentorder.set_donts(selections)
        self.dialogvermijd.hide()
        self.on_cursor_changed(self.builder.get_object('treeview1'))
        
    def on_vermijdcancel_clicked(self, *args):
        self.dialogvermijd.hide()
    
    def on_voorkeur_clicked(self, *args):
        donts   = self.currentorder.get_donts()
        prefers = self.currentorder.get_prefers()
        buttons = []
        for i in ('vis', 'gevogelte', 'kleindier', 'grootdier', 'orgaan', 'pensbot'):
            buttons.extend(self.builder.get_object('grid{0}'.format(i)).get_children())
        for button in buttons:
            label = button.get_label()
            button.set_sensitive( not label in donts)
            button.set_active( label in prefers)
        self.dialogvermijd.set_title('Kies voorkeursmaken voor {0}'.format(self.currentorder.get_animal()))
        self.donts_or_prefer = 'prefer'
        st = self.builder.get_object('vermijdstatus')
        st.pop(0)
        st.push(0, 'voorkeursmaken: {0}'.format(', '.join(prefers)))
        self.dialogvermijd = self.builder.get_object('dialogvermijd')
        self.dialogvermijd.show_all()
        self.dialogvermijd.run()
                
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
        
    def on_print( self, *args ):
        #warning( 'printing results voor {0},{1}'.format(self.store[self.position][1],self.store[self.position][2]),
        #        self.window)
        f = file('/tmp/wizardprint','w')
        tb = self.buffer
        f.write(tb.get_text(tb.get_start_iter(), tb.get_end_iter(), True))
        f.close()
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
        os.rename('../test/orders.csv', '../test/orders.prev' )
        orderfile = file('../test/orders.csv', 'w')
        orderfile.write(self.oervoer.orderhead)
        for order in self.oervoer.ordlist:
            orderfile.write(order.get_base()+','
                            +','.join(order.get_donts())
                            +',|,'
                            +','.join(order.get_prefers())
                            +'\n')
        orderfile.close()    
        Gtk.main_quit()
        
    def on_random_toggled(self, button):
        self.oervoer.set_random(button.get_active())
        if button.get_active():
            warning( 'Vanaf nu is de productkeuze evenredig met de hoeveelheid.\nProductkeuze houdt wel rekening met de voorkeurlijst.', self.window)
            button.set_label('evenredig')
        else:
            warning( 'Vanaf nu is de productkeuze gelijkmatig.\nProductkeuze houdt wel rekening met de voorkeurlijst.', self.window)
            button.set_label('gelijkmatig')

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
        self.builder.get_object('treeview1').set_rules_hint(True)

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
                          '{0}'.format(order.get_factor()),
                          '{0}'.format(order.get_package()), 
                          True,
                          'beide'
                          ])
    
    def about_activate(self, action):
        about_dlg = self.builder.get_object('aboutdialog1')
        about_dlg.run()
        about_dlg.hide()

    def quit_activate(self, action):
        Gtk.main_quit()


if __name__ == '__main__':
    builder = BuilderApp()
    Gtk.main()

