'''
Created on Jan 31, 2015

@author: mshepher
'''

from django.conf.urls import patterns, url

from wizard import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^home$', views.HomePageView.as_view(), name='home'),
    url(r'^(?P<order_id>\d+)/$', views.order, name='order'),
    url(r'^importorders$', views.ImportOrders.as_view(), name='importorders'),
    url(r'^importproducts$', views.order, name='importproducts'),
    url(r'^importpets$', views.order, name='importpets'),
    url(r'^orders$', views.order, name='orders'),
    url(r'^pets$', views.pets, name='pets'),
    url(r'^products$', views.productlist, name='productlist'),
    url(r'^(?P<order_id>\d+)/picklist/$', views.picklist, name='picklist'),
    url(r'^(?P<delivery_id>\d+)/brief/$', views.brief, name='brief'),
    url(r'^(?P<pet_id>\d+)/pet/$', views.pet, name='pet'),
    
)