from django.contrib import admin
from wizard.models import Owner, Pet, Taste, Globals, Package, Ras, Order, MeatType, prefers, Donts, Product, Delivery, PickList
# Register your models here.

admin.site.register((Owner, Pet, Taste, Globals, Package, Ras, Order, MeatType, prefers, Donts, Product, Delivery, PickList))

