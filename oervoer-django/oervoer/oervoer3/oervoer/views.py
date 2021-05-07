from django.contrib.auth import authenticate, login
from django.urls import reverse
from django.http.response import Http404, HttpResponseRedirect
from django.shortcuts import render
from django.views import generic
from django.views.generic import View
from django_tables2 import RequestConfig
import time
from datetime import date, timedelta
import traceback

from . import logger
from .oervoerexception import OervoerException
from .brains.oervoer.oervoer import Delivery as oervoerdelivery
from .brains.oervoer.oervoer import Oervoer
from .forms import PetForm, LoginForm
from .models import PickList, Ras, Order, Delivery, Pet, Product, Taste, Donts, prefers
from .tables import TasteTable, ProductTable, OrderTable, OrderTable2, PetTable
from .tables import PickListTable, BriefTable

from . import importoervoer

# global
orders = None
oervoer = None


class HomePageView(generic.TemplateView):
    template_name = 'home.html'

    def __init__(self, *args, **kwargs):
        super(HomePageView, self).__init__(args, kwargs)
        self.oervoer = Oervoer(None, None, None)

    def get_oervoer(self):
        return self.oervoer


def index(request):
    if request.user.is_authenticated:
        latest_order_list = Order.objects.filter(status__in=('processing', 'pending'))
        table = []
        for order in latest_order_list:

            try:
                Delivery.objects.get(order=order)
                st = Delivery.objects.get(order=order).status
            except Delivery.DoesNotExist:
                st = 'geen'
            ispuppy = date.today() - order.pet.birthdate < timedelta(365)
            table.append({'id': order.id, 'owner': order.owner, 'pet': order.pet,
                          'package': order.package,
                          'weight': order.weight, 'date': order.date,
                          'status': order.status,
                          'delivery_status': st, 'jonkie': ispuppy,
                          'ras': order.pet.ras, 'birthdate': order.pet.birthdate,
                          'newpet': order.newpet})

        context = {
            'latest_order_list': latest_order_list, 'table': OrderTable2(table),
            'title': 'Order List'}
        return render(request=request, template_name='index.html', context=context)
    else:
        return HttpResponseRedirect(reverse('login'))


def pets(request):
    pet_list = Pet.objects.all()
    context = {
        'latest_order_list': pet_list, 'table': PetTable(pet_list),
        'title': 'Pet List'
    }
    return render(request=request, template_name='index.html',
                  context=context)


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
    latest_order_list = Order.objects.filter(status__in=('processing', 'pending'))
    table = OrderTable(latest_order_list)
    return render(request, "index.html", {"title": "Order list", "table": table})


def get_delivery(order):
    global oervoer
    try:
        # try to get the existing delivery and recreate a table with it
        logger.info('get delivery for order{}'.format(order.id))
        delivery = Delivery.objects.get(order=order)
        picklist = delivery.picklist_set.all()
        table = []

        for pl in picklist:
            table.append({'vleestype': pl.product.vlees,
                          'sku': pl.product.sku,
                          'name': pl.product.name,
                          'shelf': pl.product.shelf,
                          'aantal': pl.number,
                          'gram': pl.product.weight})
        return delivery, PickListTable(table), []

    except Delivery.DoesNotExist:
        logger.info('making new delivery for {}'.format(order))
        if not oervoer:
            try:
                logger.info('initializing oervoer')
                oervoer = Oervoer(None, None, None)
                oervoer.parse_products()
            except:
                logger.error('can\'t init oervoer!')
                traceback.print_exc()
                raise OervoerException("Unable to start oervoer brain.")
        try:
            oervoer.prodlists = {}
            oervoer.parse_products()
            result = oervoer.process_order(order)
            d = oervoerdelivery('', order, result)
            table = d.bol()
            logger.info('table for order {} generated'.format(order))
        except:
            logger.error('cannot process order')
            traceback.print_exc()
            raise OervoerException("Unable to process order {}".format(order))
        else:
            delivery = Delivery(order=order, status='PRE',
                                date=time.strftime('%Y-%m-%d'), brief=getBrief(order))
            delivery.save()
            return delivery, table, oervoer.exceptions


def getBrief(order):
    """get the template for a brief from the data dir"""
    filename = 'data/brief-{}-{}.txt'.format(order.pet.ras, order.package)
    return open(filename, 'r').read()


def picklist(request, order_id):
    global oervoer

    def picklistfound(row, delivery, picklists):
        """try to locate the picklist before trying an add."""

        found = False
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
        retry = True
        try:
            delivery = Delivery.objects.get(order=order)
            if request.POST.get('save'):
                delivery.status = 'DELIVERED'
                delivery.save()
                if not oervoer:
                    try:
                        logger.info('initializing oervoer')
                        oervoer = Oervoer(None, None, None)
                        oervoer.parse_products()
                        logger.info('success!')
                    except:
                        logger.error('can\'t init oervoer!')
                        traceback.print_exc()
                        raise OervoerException("Unable to start oervoer brain.")
                oervoer.update_inventory(delivery)

                retry = False
            elif request.POST.get('andere'):
                delivery.delete()
                retry = True
            else:
                logger.error('what de heck was pushed?')
        except Delivery.DoesNotExist:
            logger.error('delivery does not exist')
        if retry:
            return HttpResponseRedirect(
                reverse('picklist', kwargs={'order_id': order_id}))
        else:
            return HttpResponseRedirect(reverse('index'))

    # first GET
    else:
        delivery, table, exceptions = get_delivery(order)
        # request.session['comments'] = exceptions
        if table:
            picklists = delivery.picklist_set.all()
            for row in table.rows:
                # try to get the picklist:
                if not picklistfound(row, delivery, picklists):
                    try:
                        product = Product.objects.get(sku=row.record['sku'])
                        picklist = PickList(delivery=delivery, product=product,
                                            number=row.record['aantal'])
                        picklist.save()
                    except Product.DoesNotExist:
                        logger.error('DB error, cannot fetch product {} {} {}'.format(
                            row.record['sku'], order_id, delivery.id))
                        continue
                    except Product.MultipleObjectsReturned:
                        logger.error('DB error, double product with sku {}'.format(
                            row.record['sku']))
                        continue

            RequestConfig(request, paginate=False).configure(table)

            vermijdlijst = ','.join([i.taste.taste for i in order.pet.donts_set.all()])
            return render(request, 'picklist.html', {'delivery_id': delivery.id,
                                                     'delivery_pre': delivery.status == 'PRE',
                                                     'title': 'Picklist voor {}'.format(
                                                         order.pet),
                                                     'order_id': order_id,
                                                     'table': table,
                                                     'datum': time.strftime('%Y-%m-%d'),
                                                     'dier': order.pet.ras.ras,
                                                     'pakket': order.package,
                                                     'gewicht_dier': order.pet.weight,
                                                     'gewicht_pakket': order.weight,
                                                     'vermijd': vermijdlijst,
                                                     'maaltijd': f'{order.pet.get_meal_size() * 1000:0.0f}',
                                                     'eigenaar': order.owner,
                                                     'diernaam': order.pet.name,
                                                     'totaal': sum
                                                     ([i.record['gram'] * i.record[
                                                         'aantal'] for i in
                                                       table.rows])})
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
        logger.info('get delivery {}'.format(delivery_id))
        delivery = Delivery.objects.get(pk=delivery_id)
        picklist = delivery.picklist_set.all()
        order = Order.objects.get(id=delivery.order.id)
        pet = order.pet
        table = []
        for pl in picklist:
            table.append({'vleestype': pl.product.vlees,
                          'name': pl.product.name,
                          'aantal': pl.number})
        table = BriefTable(table)
    except Delivery.DoesNotExist:
        raise Http404('Can\'t find delivery {}'.format(delivery_id))
    context = {
        'datum': time.strftime('%d-%m-%Y'),
        'brief_template': 'brief-{}-{}.html'.format(
            order.pet.ras, order.package),
        'delivery': delivery, 'order': order, 'pet': pet,
        'table': table,
        'maaltijd': f'{pet.get_meal_size() * pet.profile.NRMEALS * 1000:0.0f}'
    }
    return render(request=request, template_name="brief.html", context=context)


def maketable(request, donts, obj):
    tab = []
    d = {}
    for i, element in enumerate(obj):
        col = i % 8
        d['taste{}'.format(col + 1)] = element
        d['check{}'.format(col + 1)] = element in donts
        if col == 7:
            tab.append(d)
            d = {}
    tab.append(d)
    tb = TasteTable(tab)
    RequestConfig(request).configure(tb)

    return tb


class LoginView(View):
    form_class = LoginForm
    template_name = 'login.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form, 'errors': ''})

    def post(self, request):
        form = self.form_class(request.POST)

        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                logger.info('user {} authenticated {}'.format(username,
                                                              request.user.is_authenticated))
                return HttpResponseRedirect(reverse('index'))
            else:
                logger.error('user {} not active'.format(username))
        else:
            logger.error('user {} not authenticated'.format(username))

        return render(request, self.template_name, {'form': form,
                                                    'errors': 'user {} is not registered or password wrong'.format(
                                                        request.POST['username'])})


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
                    logger.error('can\'t save the taste {} for pet {}'.format(taste_id,
                                                                              pet))
        for taste in donts:
            if not taste.id in taste_ids_from_post:
                try:
                    dont = Donts.objects.get(pet=pet, taste=taste)
                    dont.delete()
                except Donts.DoesNotExist:
                    logger.error('can\'t find dont for {} {}'.format(pet, taste))
        if form.is_valid():
            form.save()
        else:
            logger.error('did not validate: ')
            logger.error(form.errors)
            # must return here to the pet page and display the errors!!!

        return HttpResponseRedirect(reverse('pets'))
    else:

        form = PetForm(instance=pet)

        fish = maketable(request, donts, Taste.objects.filter(is_fish=True))
        fowl = maketable(request, donts, Taste.objects.filter(is_fowl=True))
        big = maketable(request, donts, Taste.objects.filter(is_big=True))
        small = maketable(request, donts, Taste.objects.filter(is_small=True))
        organ = maketable(request, donts, Taste.objects.filter(is_organ=True))
        other = maketable(request, donts, Taste.objects.filter(is_else=True))

        return render(request, 'pet.html',
                      {'is_hond': pet.ras == Ras.objects.get(ras='HOND'),
                       'pet_id': pet_id,
                       'form': form, 'title': 'Pet form voor {}'.format(pet.name),
                       'fish': fish, 'fowl': fowl, 'big': big, 'small': small,
                       'organ': organ, 'other': other
                       })


def comments(request):
    return HttpResponseRedirect(reverse('pets'))


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
                    logger.error('can\'t save the like taste {} for pet {}'.format(
                        taste_id, pet))
        for taste in likes:
            if not taste.id in taste_ids_from_post:
                try:
                    like = prefers.objects.get(pet=pet, taste=taste)
                    like.delete()
                except prefers.DoesNotExist:
                    logger.error('can\'t find prefer for {} {}'.format(pet, taste))
        if form.is_valid():
            form.save()
        else:
            logger.error('did not validate: ')
            logger.error(form.errors)
            # must return here to the pet page and display the errors!!!

        return HttpResponseRedirect(reverse('pets'))
    else:

        form = PetForm(instance=pet)

        fish = maketable(request, likes, Taste.objects.filter(is_fish=True))
        fowl = maketable(request, likes, Taste.objects.filter(is_fowl=True))
        big = maketable(request, likes, Taste.objects.filter(is_big=True))
        small = maketable(request, likes, Taste.objects.filter(is_small=True))
        organ = maketable(request, likes, Taste.objects.filter(is_organ=True))
        other = maketable(request, likes, Taste.objects.filter(is_else=True))

        return render(request, 'pet_likes.html',
                      {'is_hond': pet.ras == Ras.objects.get(ras='HOND'),
                       'pet_id': pet_id,
                       'form': form, 'title': 'Pet voorkeuren voor {}'.format(pet.name),
                       'fish': fish, 'fowl': fowl, 'big': big, 'small': small,
                       'organ': organ, 'other': other
                       })
