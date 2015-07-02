'''
Created on Apr 16, 2015

@author: mshepher
'''
from datetime import datetime
from django.core.urlresolvers import reverse
from django.http.response import HttpResponseRedirect
from django_tables2.views import SingleTableView
from pprint import pprint

from wizard import importoervoer
from wizard.models import Globals, Owner, Ras, Pet, Package, Order, Product
from wizard.tables import OrderTable, ProductTable


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
        context.update({'table': OrderTable(self.get_table_data()), 'title': 'Order List'})
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
                    pprint(owner)
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
                o = Order(id=order['id'],owner=owner, pet=pet, package=package,weight=order['gewicht_pak'], status=order['status'], date = datetime.now() )
                o.save()   
            #o = Order( id=order.order_id, owner=order.custid, pet=pet_id, package=package, weight=order_weight, date=today, status=order.status)
        return HttpResponseRedirect(reverse('index'))
        #return HttpResponse(loader.get_template('index.html').render(self.get_context_data()))
        

class ImportProducts(SingleTableView):
    table_class = OrderTable

    def __init__(self, *args, **kwargs):
        super(ImportProducts, self).__init__()
        user = 'bvdheide_micha'
        pw = 'lelijkgedrocht'
        self.products = []
        imp = importoervoer.ImportProds(user, pw)
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
        #print request
        profile=Globals.objects.get(DESC='Standaard') # get the standard profile
        Product.objects.all().delete()
        for product in self.products:
            pprint(product)
            #{'id','name','sku','qty','smaak','vlees','shelf','weight', 'verpakking', kat_hond})
            p = Product(id=product['id'], name=product['name'],
                        sku=product['sku'], qty=product['qty'],
                        smaak=product['smaak'], vlees=product['vlees'],
                        shelf=product['shelf'], weight=product['weight'],
                        verpakking=product['verpakking'], kat_hond=product['kat_hond'] )
            p.save()
        return HttpResponseRedirect(reverse('productlist'))
        #return HttpResponse(loader.get_template('index.html').render(self.get_context_data()))

