
import datetime
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.http.response import Http404, HttpResponseRedirect
from django.shortcuts import render
from django.template import RequestContext, loader
from django.views import generic
from django_tables2   import RequestConfig, SingleTableView
import pprint
import time
import traceback

from wizard.brains.oervoer.oervoer import Delivery as oervoerdelivery
from wizard.brains.oervoer.oervoer import Oervoer
from wizard.forms import PetForm
from wizard.models import PickList, Ras, Package, Order, Delivery, Pet, Product, Owner, Globals, Taste, Donts
from wizard.tables import TasteTable, ProductTable, OrderTable, OrderTable2, PetTable

from . import importoervoer


# global
orders = None
oervoer = None

class HomePageView(generic.TemplateView):
    template_name = 'home.html'
    def __init__(self, *args, **kwargs):
        super (HomePageView, self).__init__(args, kwargs)
        self.oervoer = Oervoer(None, None, None)
    
    def get_oervoer(self):
        return self.oervoer

class ImportOrders(SingleTableView):
    table_class = OrderTable

    def __init__(self, *args, **kwargs):
        super(ImportOrders, self).__init__()
        user = 'bvdheide_micha'
        pw = 'lelijkgedrocht'
        self.orders = []
        imp = importoervoer.ImportOrders(user, pw)
        if imp.connect():
            self.orders = imp.importtable()
        
    def get_table_data(self):
        return self.orders
    
    def get_queryset(self):
        return self.orders
    
    def get_template_names(self):
        return ('importorders.html')
    
    def get_context_data(self, **kwargs):
        context = super(ImportOrders, self).get_context_data(**kwargs)
        context.update({'table': OrderTable(self.get_table_data()), 'title:': 'Order List'})
        return context
    
    def post(self, request, *args, **kwargs):
        #print request
        profile=Globals.objects.get(DESC='Standaard') # get the standard profile
        for order in self.orders:
            #pprint.pprint(order)
            if not order['customer_id']:
                order['customer_id'] = 9999
                owner=Owner(id=9999, name=order['customer_name']) # fake owner!!
                owner.save()
                print 'renegate owner {}{} generated!'.format(owner.pk,owner.name)
            else:
                try:
                    owner = Owner.objects.get(id=order['customer_id']) # get the owner or create
                except Owner.DoesNotExist:
                    owner = Owner(id=order['customer_id'], name=order['customer_name'])
                    pprint.pprint(owner)
                    owner.save()
            try: 
                ras = Ras.objects.get(ras=order['ras']) # get the pet race or HOND
            except Ras.DoesNotExist:
                ras = Ras.objects.get(ras='HOND')
                print 'order with bad pet.'
            try:                                        # get the pet or create
                pet = Pet.objects.get(name=order['name'])
            except Pet.DoesNotExist:
                pet = Pet(name=order['name'], weight=order['weight'], ras=ras, owner=owner, factor=1.0, profile=profile)
                pet.save()
             #{'id','status','customer_id','customer_name','pakket','ras','gewicht_pak','name','weight'})
            try:                                        #get the package or create          
                package = Package.objects.get(type=order['pakket'])
            except Package.DoesNotExist:
                package = Package.objects.get(id=0)
                print 'order with bad package.'
            try:
                o = Order.objects.get(pk=int(order['id']))
            except Order.DoesNotExist:
                o = Order(id=order['id'],owner=owner, pet=pet, package=package,weight=order['gewicht_pak'], status=order['status'], date = datetime.datetime.now() )
                o.save()   
            #o = Order( id=order.order_id, owner=order.custid, pet=pet_id, package=package, weight=order_weight, date=today, status=order.status)
        return HttpResponseRedirect(reverse('index'))
        #return HttpResponse(loader.get_template('index.html').render(self.get_context_data()))
        
    
def index(request):
    latest_order_list = Order.objects.filter(status__in = ('processing','pending'))
    template = loader.get_template('index.html')
    context = RequestContext(request, {
        'latest_order_list': latest_order_list,'table': OrderTable2(latest_order_list),
        'title':'Order List'})
    return HttpResponse(template.render(context))

def pets(request):
    pet_list = Pet.objects.all()
    template = loader.get_template('index.html')
    context = RequestContext(request, {
        'latest_order_list': pet_list,'table': PetTable(pet_list),
        'title':'Pet List'})
    return HttpResponse(template.render(context))

def allorders(request, order_id):
    global orders
    
    if not orders:
        user = 'bvdheide_micha'
        pw = 'lelijkgedrocht'
        imp = importoervoer.ImportOrders(user, pw)
        if imp.connect():
            orders = imp.importallorders()
    
    table = OrderTable(orders)
    RequestConfig(request).configure(table)
    return render(request, "index.html", {"title": "Order list", "table": table})

def order(request, order_id):
    latest_order_list = Order.objects.filter(status__in = ('processing','pending'))
    table = OrderTable(latest_order_list)
    RequestConfig(request).configure(table)
    return render(request, "index.html", {"title": "Order list", "table": table})

def get_delivery(order):
    global oervoer
    if not oervoer:
        try:
            print 'initializing oervoer'
            oervoer = Oervoer(None,None,None)
            oervoer.parse_products()
            print 'success!'
        except:
            print 'can\'t init oervoer!'
            traceback.print_exc()
    try:
        print 'oervoer {}'.format(oervoer)
        result = oervoer.process_order(order)
        d = oervoerdelivery('', order, result)
        table = d.bol()
        print 'table for order {} generated'.format(order)
    except:
        print 'cannot process order'
        traceback.print_exc()
    else:
        return table
    
def picklist(request, order_id):
    try:
        order = Order.objects.get(id=order_id)
    except Order.DoesNotExist:
        raise Http404('no such order {}'.format(order_id))
    table = get_delivery(order)
    if table:
        RequestConfig(request).configure(table)
        print time.strftime('%x')
        return render(request, 'picklist.html', {'title': 'Picklist voor {}'.format(order.pet), 'table': table,
                                                 'datum': time.strftime('%x'), 'dier':order.pet.ras.ras, 'pakket':order.package,
                                                 'gewicht_dier': order.pet.weight, 'gewicht_pakket':order.weight, 'vermijd': 'asdf',
                                                 'maaltijd': order.pet.get_meal_size(), 'eigenaar':order.owner, 'diernaam':order.pet.name,
                                                 'totaal': sum([i.record['gram']*i.record['aantal'] for i in table.rows])})
    else:
        raise Http404('Cannot produce the delivery for order {}'.format(order_id))

def productlist(request):
    latest_order_list = Product.objects.all()
    table = ProductTable(Product.objects.all())
    RequestConfig(request).configure(table)
    return render(request, 'index.html', {"title": "Product list", 'table': table})
                  
def brief(request, delivery_id):
    
    delivery = Delivery.objects.get(pk=delivery_id)
    order = Order.objects.get(pk=delivery.order)
    pet = Pet.objects.get(pk=order.pet)
    template = loader.get_template('brief.html')
    context = RequestContext(request, {'pet':pet})
    
    
    return HttpResponse(template.render(context))

def maketable(request, donts, obj):
    tab = []
    d = {}
    for i, element in enumerate(obj):
        col = i % 8
        d['taste{}'.format(col+1)] = element
        d['check{}'.format(col+1)] = element in donts
        if col == 7:
            tab.append(d)
            d = {}
    tab.append(d)
    tb = TasteTable(tab)
    RequestConfig(request).configure(tb)
            
    return tb

def pet(request, pet_id):
    try:
        pet = Pet.objects.get(pk=pet_id)
        donts = [i.taste for i in pet.donts_set.all()]
    except Pet.DoesNotExist:
        raise Http404('no such pet {}'.format(pet_id))
 
    if request.method == 'POST':
        dont_ids = [i.id for i in donts]
        form = PetForm(request.POST, instance=pet)
        vermijdlijst = request.POST['checked_tastes']
        
        taste_ids_from_post = [int(i) for i in vermijdlijst.split(',')[:-1]]
        for taste_id in taste_ids_from_post:
            if not taste_id in dont_ids:
                # make a new record
                try:
                    taste = Taste.objects.get(pk=taste_id)
                    dont = Donts(pet=pet, taste=taste)
                    dont.save()
                except Taste.DoesNotExist:
                    print 'can\'t save the taste {} for pet {}'.format(taste, pet)
        for taste in donts:
            if not taste.id in taste_ids_from_post:
                try:
                    dont = Donts.objects.get(pet=pet, taste=taste)
                    dont.delete()
                except Donts.DoesNotExist:
                    print 'can\'t find dont for {} {}'.format(pet, taste)
        if form.is_valid():
            form.save()
        else:
            print 'did not validate: '
            print form.errors
            # must return here to the pet page and display the errors!!!
            
        return HttpResponseRedirect(reverse('pets'))
    else:
            
        form = PetForm(instance=pet)
        
        fish  = maketable(request, donts, Taste.objects.filter(is_fish=True))
        fowl  = maketable(request, donts, Taste.objects.filter(is_fowl=True))
        big   = maketable(request, donts, Taste.objects.filter(is_big=True))
        small = maketable(request, donts, Taste.objects.filter(is_small=True))
        organ = maketable(request, donts, Taste.objects.filter(is_organ=True))
        other = maketable(request, donts, Taste.objects.filter(is_else=True))
        
        return render(request, 'pet.html', {'is_hond': pet.ras == Ras.objects.get(ras='HOND'), 'pet_id':pet_id,
            'form': form, 'title': 'Pet form voor {}'.format(pet.name), 
            'fish':fish, 'fowl':fowl, 'big':big, 'small':small, 'organ':organ, 'other':other
        })
