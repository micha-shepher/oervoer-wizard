from django.contrib import admin
from wizard.models import Owner, Pet, Taste, Globals, Package, Ras, Order, MeatType, prefers, Donts, Product, Delivery, PickList
# Register your models here.

admin.site.register((Owner, Pet, Taste, Globals, Package, Ras, Order, MeatType, prefers, Donts, Delivery))

class PickListAdmin(admin.ModelAdmin):

    fields = ['delivery', 'product', 'number']
    list_filter = ['product']
    search_fields = ['delivery__order__owner__name', 'delivery__order__pet__name', 'product__name']


admin.site.register(PickList, PickListAdmin)


class ProductAdmin(admin.ModelAdmin):
    fields = ['id', 'name', 'sku', 'qty', 'smaak', 'vlees', 'weight', 'verpakking', 'kat_hond']
    list_filter = ['vlees', 'smaak']
    search_fields = ['vlees__meat_type', 'smaak__taste']
    
admin.site.register(Product, ProductAdmin)

