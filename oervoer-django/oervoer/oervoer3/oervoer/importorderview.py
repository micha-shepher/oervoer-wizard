'''
Created on Apr 16, 2015

@author: mshepher
'''
from datetime import datetime
from django.urls import reverse
from django.http.response import HttpResponseRedirect
from django_tables2.views import SingleTableView

from oervoer.models import Globals, Owner, Ras, Pet, Package, Order, Product
from oervoer.tables import OrderTable, ProductTable
from . import importoervoer, logger


class ImportOrders(SingleTableView):
    table_class = OrderTable

    def __init__(self, *args, **kwargs):
        super(ImportOrders, self).__init__()
        self.orders = []
        self.newpets = []
        imp = importoervoer.ImportOrders()
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
        context.update({'table': OrderTable(self.get_table_data()), 'title': 'Order List'})
        return context
    
    def post(self, request, *args, **kwargs):
        #print request
        profile=Globals.objects.get(DESC='Standaard') # get the standard profile
        for order in self.orders:
            isnewpet = False
            if not order['customer_id']:
                order['customer_id'] = 9999
                owner=Owner(id=9999, name=order['customer_name']) # fake owner!!
                owner.save()
                logger.info('auto owner {}{} generated!'.format(owner.pk,
                                                                    owner.name))
            else:
                try:
                    owner = Owner.objects.get(id=order['customer_id']) # get the owner or create
                except Owner.DoesNotExist:
                    logger.info(f"new owner {order['customer_id']}, "
                                f"{order['customer_name']}")
                    owner = Owner(id=order['customer_id'], name=order['customer_name'])
                    owner.save()
            try: 
                ras = Ras.objects.get(ras=order['ras']) # get the pet race or HOND
            except Ras.DoesNotExist:
                ras = Ras.objects.get(ras='HOND')
                logger.error(f"bad pet, unknown ras {order['ras']}.")
            try:  # get the pet or create
                pet = Pet.objects.get(name__iexact=order['name'], owner=owner)
            except Pet.DoesNotExist:
                logger.info(f"new pet {order}")
                pet = Pet(name=order['name'], weight=order['weight'], ras=ras, owner=owner, factor=1.0, profile=profile,
                          birthdate=order['date'])
                try:
                    pet.save()
                    self.newpets.append(pet)
                    isnewpet = True
                except:
                    logger.error('kan pet {0} niet bewaren, want gewicht {1} wordt '
                      'geweigerd.'.format(pet.name, pet.weight))

            #{'id','status','customer_id','customer_name','pakket','ras','gewicht_pak','name','weight'})

            try:  # get the package or create
                package = Package.objects.get(type=order['pakket'])
            except Package.DoesNotExist:
                package = Package.objects.get(id=0)
                logger.error(f'order with bad package {order["pakket"]}.')

            try:
                o = Order.objects.get(pk=int(order['id']))
                o.status=order['status']
                o.save()
            except Order.DoesNotExist:
                try:
                    o = Order(id=order['id'],owner=owner, pet=pet, package=package,weight=order['gewicht_pak'],
                              status=order['status'], date = datetime.now(), newpet = isnewpet )
                    o.save()
                except ValueError:
                    logger.error('kan order niet bewaren omdat pet {0} is niet in '
                      'database.'.format(pet.name))

        return HttpResponseRedirect(reverse('index'))


class ImportProducts(SingleTableView):
    table_class = OrderTable

    def __init__(self, *args, **kwargs):
        super(ImportProducts, self).__init__()
        self.products = []
        imp = importoervoer.ImportProds()
        if imp.connect():
            self.products = imp.importtable()

    def get_table_data(self):
        return self.products

    def get_queryset(self):
        return self.products

    def get_template_names(self):
        return ('importproducts.html')

    def get_context_data(self, **kwargs):
        context = super(ImportProducts, self).get_context_data(**kwargs)
        context.update({'table': ProductTable(self.get_table_data()), 'title': 'Product List'})
        return context

    def post(self, request, *args, **kwargs):

        for product in self.products:
            if Product.objects.filter(id=product['id']).exists():
                p = Product.objects.get(id=product['id'])
                p.smaak = product['smaak']
                p.vlees = product['vlees']
                p.weight = product['weight']
                p.kat_hond = product['kat_hond']
                p.verpakking = product['verpakking']
                p.qty = product['qty']
                p.shelf = product['shelf']
            else:
            #{'id','name','sku','qty','smaak','vlees','shelf','weight', 'verpakking', kat_hond})
                p = Product(id=product['id'], name=product['name'],
                        sku=product['sku'], qty=product['qty'],
                        smaak=product['smaak'], vlees=product['vlees'],
                        shelf=product['shelf'], weight=product['weight'],
                        verpakking=product['verpakking'], kat_hond=product['kat_hond'] )
            p.save()
        # now zero the quantity of all products in the database who are not imported.
        imported = [p['id'] for p in self.products]
        for p in Product.objects.all():
            if not p.id in imported:
                logger.info(f'zeroing qty old product  {p.id}, {p.name}, {p.qty}')
                p.qty = 0
                p.save()


        return HttpResponseRedirect(reverse('productlist'))

