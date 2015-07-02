
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.http.response import Http404, HttpResponseRedirect
from django.shortcuts import render
from django.template import RequestContext, loader
from django.views import generic
from django_tables2   import RequestConfig
import time
import traceback

from oervoerexception import OervoerException
from wizard.brains.oervoer.oervoer import Delivery as oervoerdelivery
from wizard.brains.oervoer.oervoer import Oervoer
from wizard.forms import PetForm
from wizard.models import PickList, Ras, Order, Delivery, Pet, Product, Taste, Donts, prefers
from wizard.tables import TasteTable, ProductTable, OrderTable, OrderTable2, PetTable
from wizard.tables import PickListTable, BriefTable

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

def index(request):
    latest_order_list = Order.objects.filter(status__in = ('processing','pending'))
    template = loader.get_template('index.html')
    table = []
    for order in latest_order_list:
        try:
            Delivery.objects.get(order=order)
            st = Delivery.objects.get(order=order).status
        except Delivery.DoesNotExist:
            st = 'geen'
        table.append({'id': order.id, 'owner': order.owner, 'pet': order.pet, 'package':order.package,
             'weight': order.weight, 'date': order.date, 'status': order.status, 'delivery_status': st, 'ras': order.pet.ras})

    context = RequestContext(request, {
        'latest_order_list': latest_order_list,'table': OrderTable2(table),
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
    try:
        # try to get the existing delivery and recreate a table with it
        print 'get delivery for order{}'.format(order.id)
        delivery = Delivery.objects.get(order=order)
        picklist = delivery.picklist_set.all()
        table = []

        for pl in picklist:
            table.append({'vleestype':pl.product.vlees,
                          'sku':      pl.product.sku,
                          'name':     pl.product.name,
                          'shelf':    pl.product.shelf,
                          'aantal':   pl.number,
                          'gram':     pl.product.weight})
        return delivery, PickListTable(table)
    
    except Delivery.DoesNotExist:
        print 'making new delivery for {}'.format(order)    
        if not oervoer:
            try:
                print 'initializing oervoer'
                oervoer = Oervoer(None,None,None)
                oervoer.parse_products()
                print 'success!'
            except:
                print 'can\'t init oervoer!'
                traceback.print_exc()
                raise OervoerException("Unable to start oervoer brain.")
        try:
            print 'oervoer {}'.format(oervoer)
            result = oervoer.process_order(order)
            d = oervoerdelivery('', order, result)
            table = d.bol()
            print 'table for order {} generated'.format(order)
        except:
            print 'cannot process order'
            traceback.print_exc()
            raise OervoerException("Unable to process order {}".format(order))
        else:
            delivery = Delivery(order = order, status = 'PRE', date = time.strftime('%Y-%m-%d'), brief = getBrief(order))
            delivery.save()
            return delivery, table
        
def getBrief(order):
    '''get the template for a brief from the data dir'''
    filename = 'data/brief-{}-{}.txt'.format(order.pet.ras, order.package)
    return file(filename,'r').read()

def picklist(request, order_id):

    def picklistfound(row, delivery, picklists):
        '''try to locate the picklist before trying an add.'''

        found  = False
        for pl in picklists:
            if pl.product.sku == row.record['sku'] and \
               pl.delivery.id == delivery.id:
                found = True
                break
        return found

    # get the order
    try:
        order = Order.objects.get(id=order_id)
    except Order.DoesNotExist:
        raise Http404('no such order {}'.format(order_id))
    # save pressed
    if request.method == 'POST':
        # OK, change and update the delivery!
        try:

            delivery = Delivery.objects.get(order=order)
            if request.POST.get('save'):
                delivery.status = 'DELIVERED'
                delivery.save()
                retry = False
            elif request.POST.get('andere'):
                delivery.delete()
                retry = True
            else:
                print 'what de heck was pushed?'
        except Delivery.DoesNotExist:
            print 'delivery does not exist'
        if retry:
            return HttpResponseRedirect(reverse('picklist', kwargs={'order_id':order_id}))
        else:
            return HttpResponseRedirect(reverse('index'))

    # first GET
    else:
        delivery, table = get_delivery(order)
        if table:
            picklists = delivery.picklist_set.all()
            for row in table.rows:
                product = Product.objects.get(sku=row.record['sku'])
                # try to get the picklist:
                if not picklistfound(row, delivery, picklists):
                    picklist = PickList( delivery=delivery, product=product, number=row.record['aantal'])
                    picklist.save()

            RequestConfig(request, paginate=False).configure(table)

            vermijdlijst = ','.join([i.taste.taste for i in order.pet.donts_set.all()])
            return render(request, 'picklist.html', {'delivery_id': delivery.id,
                                                     'delivery_pre': delivery.status == 'PRE',
                                                     'title': 'Picklist voor {}'.format(order.pet), 
                                                     'order_id': order_id, 'table': table,
                                                     'datum': time.strftime('%Y-%m-%d'), 'dier':order.pet.ras.ras, 'pakket':order.package,
                                                     'gewicht_dier': order.pet.weight, 'gewicht_pakket':order.weight, 'vermijd': vermijdlijst,
                                                     'maaltijd': order.pet.get_meal_size(), 'eigenaar':order.owner, 'diernaam':order.pet.name,
                                                     'totaal': sum
                                                     ([i.record['gram'] *i.record['aantal'] for i in table.rows])})
        else:
            raise Http404('Cannot produce the delivery for order {}'.format(order_id))

def productlist(request):
    latest_order_list = Product.objects.all()
    table = ProductTable(Product.objects.all())
    RequestConfig(request).configure(table)
    return render(request, 'index.html', {"title": "Product list", 'table': table})
                  
def brief(request, delivery_id):
    
    try:
        # try to get the existing delivery and recreate a table with it
        print 'get delivery {}'.format(delivery_id)
        delivery = Delivery.objects.get(pk=delivery_id)
        picklist = delivery.picklist_set.all()
        order = Order.objects.get(id=delivery.order.id)
        pet = order.pet
        template = loader.get_template('brief.html')
        table = []
        for pl in picklist:
            table.append({'vleestype':pl.product.vlees,
                          'name':     pl.product.name,
                          'aantal':   pl.number})
        table = BriefTable(table)
    except Delivery.DoesNotExist:
        raise Http404('Can\'t find delivery {}'.format(delivery_id))
    RequestConfig(request, paginate=False).configure(table)
    context = RequestContext(request, {'datum': time.strftime('%d-%m-%Y'), 
                                       'brief_template': 'brief-{}-{}.html'.format(order.pet.ras, order.package), 
                                       'delivery':delivery,'order': order, 'pet':pet, 'table':table,
                                       'maaltijd':pet.profile.get_factor(pet.ras.ras) *float(pet.weight) *1000})
    return HttpResponse(template.render(context))

def maketable(request, donts, obj):
    tab = []
    d = {}
    for i, element in enumerate(obj):
        col = i % 8
        d['taste{}'.format(col +1)] = element
        d['check{}'.format(col +1)] = element in donts
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

def pet_likes(request, pet_id):
    try:
        pet = Pet.objects.get(pk=pet_id)
        likes = [i.taste for i in pet.prefers_set.all()]
    except Pet.DoesNotExist:
        raise Http404('no such pet {}'.format(pet_id))
 
    if request.method == 'POST':
        likes_ids = [i.id for i in likes]
        form = PetForm(request.POST, instance=pet)
        likelijst = request.POST['checked_tastes']
        
        taste_ids_from_post = [int(i) for i in likelijst.split(',')[:-1]]
        for taste_id in taste_ids_from_post:
            if not taste_id in likes_ids:
                # make a new record
                try:
                    taste = Taste.objects.get(pk=taste_id)
                    like = prefers(pet=pet, taste=taste)
                    like.save()
                except Taste.DoesNotExist:
                    print 'can\'t save the like taste {} for pet {}'.format(taste, pet)
        for taste in likes:
            if not taste.id in taste_ids_from_post:
                try:
                    like = prefers.objects.get(pet=pet, taste=taste)
                    like.delete()
                except prefers.DoesNotExist:
                    print 'can\'t find prefer for {} {}'.format(pet, taste)
        if form.is_valid():
            form.save()
        else:
            print 'did not validate: '
            print form.errors
            # must return here to the pet page and display the errors!!!
            
        return HttpResponseRedirect(reverse('pets'))
    else:
            
        form = PetForm(instance=pet)
        
        fish  = maketable(request, likes, Taste.objects.filter(is_fish=True))
        fowl  = maketable(request, likes, Taste.objects.filter(is_fowl=True))
        big   = maketable(request, likes, Taste.objects.filter(is_big=True))
        small = maketable(request, likes, Taste.objects.filter(is_small=True))
        organ = maketable(request, likes, Taste.objects.filter(is_organ=True))
        other = maketable(request, likes, Taste.objects.filter(is_else=True))
        
        return render(request, 'pet_likes.html', {'is_hond': pet.ras == Ras.objects.get(ras='HOND'), 'pet_id':pet_id,
            'form': form, 'title': 'Pet voorkeuren voor {}'.format(pet.name), 
            'fish':fish, 'fowl':fowl, 'big':big, 'small':small, 'organ':organ, 'other':other
        })
