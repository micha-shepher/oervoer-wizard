'''
Created on Jan 31, 2015

@author: mshepher
'''
from django.urls import path

from . import views
from .importorderview import ImportOrders, ImportProducts

urlpatterns = [
    path('', views.index, name='index'),
    path('home', views.HomePageView.as_view(), name='home'),
    path('<int:order_id>', views.order, name='order'),
    path('importorders', ImportOrders.as_view(), name='importorders'),
    path('importproducts', ImportProducts.as_view(), name='importproducts'),
    path('importpets', views.order, name='importpets'),
    path('orders', views.order, name='orders'),
    path('pets', views.pets, name='pets'),
    path('products', views.productlist, name='productlist'),
    path('<int:order_id>/picklist/', views.picklist, name='picklist'),
    path('<int:delivery_id>/brief/', views.brief, name='brief'),
    path('<int:pet_id>/pet/', views.pet, name='pet'),
    path('<int:pet_id>/pet_likes/', views.pet_likes, name='pet_likes'),
    path('login', views.LoginView.as_view(), name='login'),
    path('comments', views.comments, name='comments'),
]