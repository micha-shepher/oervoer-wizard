'''
Created on Apr 4, 2015

@author: mshepher
'''
from django.utils.safestring import mark_safe
from django_tables2.utils import A  # alias for Accessor

import django_tables2 as tables
from models import Taste, Product, Order, Owner, Pet, PickList


# from setuptools.dist import sequence
class ProductTable(tables.Table):
    # id = tables.Column()
    # name = tables.Column()
    # sku = tables.Column()
    # qty = tables.Column()
    # smaak = tables.Column()
    # vlees = tables.Column()
    # shelf = tables.Column()
    # weight = tables.Column()
    # verpakking = tables.Column()
    # kat_hond = tables.Column()
    class Meta:
        model = Product
        # add class="paleblue" to <table> tag
        attrs = {"class": "paleblue"}

class OrderTable2(tables.Table):
    id = tables.LinkColumn('picklist', args=[A('id')])
    class Meta:
        model = Order
        # add class="paleblue" to <table> tag
        attrs = {"class": "paleblue"}
    
class OrderTable(tables.Table):
    id = tables.LinkColumn('picklist', args=[A('id')])
    status = tables.Column()
    customer_id = tables.Column(visible=False)
    customer_name = tables.Column()
    pakket = tables.Column()
    ras = tables.Column()
    gewicht_pak = tables.Column()
    name = tables.Column()
    weight = tables.Column()
    class Meta:
    #    model = Order
        # add class="paleblue" to <table> tag
        attrs = {"class": "paleblue"}

class OwnerTable(tables.Table):
    class Meta:
        model = Owner
        # add class="paleblue" to <table> tag
        attrs = {"class": "paleblue"}

class PetTable(tables.Table):
    name = tables.LinkColumn('pet', args=[A('id')])
    class Meta:
        model = Pet
        # add class="paleblue" to <table> tag
        attrs = {"class": "paleblue"}

class PickListTable(tables.Table):
    vleestype = tables.Column()
    sku = tables.Column()
    name = tables.Column()
    shelf = tables.Column()
    aantal = tables.Column()
    gram = tables.Column()
    
    class Meta:
        # add class="paleblue" to <table> tag
        attrs = {"class": "paleblue"}


class TasteTable(tables.Table):
    check1 = tables.CheckBoxColumn(accessor='check1')
    taste1 = tables.Column()
    check2 = tables.CheckBoxColumn(accessor='check2')
    taste2 = tables.Column()
    check3 = tables.CheckBoxColumn(accessor='check3')
    taste3 = tables.Column()
    check4 = tables.CheckBoxColumn(accessor='check4')
    taste4 = tables.Column()
    check5 = tables.CheckBoxColumn(accessor='check5')
    taste5 = tables.Column()
    check6 = tables.CheckBoxColumn(accessor='check6')
    taste6 = tables.Column()
    check7 = tables.CheckBoxColumn(accessor='check7')
    taste7 = tables.Column()
    check8 = tables.CheckBoxColumn(accessor='check8')
    taste8 = tables.Column()
    checkbox = '<input class="nameCheckBox" value={} name="{}" type="checkbox" {} onchange="markcb()"/>'
    def render_check1(self, record):
        return mark_safe(TasteTable.checkbox.format(record['taste1'].id, record['taste1'].taste, ('','checked')[record['check1']]))
    def render_check2(self, record):                        
        return mark_safe(TasteTable.checkbox.format(record['taste2'].id, record['taste2'].taste, ('','checked')[record['check2']]))
    def render_check3(self, record):                        
        return mark_safe(TasteTable.checkbox.format(record['taste3'].id, record['taste3'].taste, ('','checked')[record['check3']]))
    def render_check4(self, record):                        
        return mark_safe(TasteTable.checkbox.format(record['taste4'].id, record['taste4'].taste, ('','checked')[record['check4']]))
    def render_check5(self, record):                        
        return mark_safe(TasteTable.checkbox.format(record['taste5'].id, record['taste5'].taste, ('','checked')[record['check5']]))
    def render_check6(self, record):                        
        return mark_safe(TasteTable.checkbox.format(record['taste6'].id, record['taste6'].taste, ('','checked')[record['check6']]))
    def render_check7(self, record):                        
        return mark_safe(TasteTable.checkbox.format(record['taste7'].id, record['taste7'].taste, ('','checked')[record['check7']]))
    def render_check8(self, record):                        
        return mark_safe(TasteTable.checkbox.format(record['taste8'].id, record['taste8'].taste, ('','checked')[record['check8']]))
    
    class Meta:
        # model = Taste
        attrs = {"class": "paleblue"}
