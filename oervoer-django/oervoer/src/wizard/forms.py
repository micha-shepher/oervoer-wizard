'''
Created on Apr 5, 2015

@author: mshepher
'''

from django import forms
from wizard.models import Delivery, Order, Pet
from django.contrib.auth.models import User


class OrderImportForm(forms.Form):
    your_name = forms.DateField()

class LoginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username', 'password']

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['id', 'owner', 'pet', 'package', 'weight', 'date', 'status']

class PicklistForm(forms.Form):
    date = forms.DateField()
    dier = forms.CharField()
    pakket = forms.CharField()
    gewicht_dier = forms.DecimalField()
    gewicht_pakket = forms.DecimalField()
    vermijd = forms.CharField()
    maaltijd = forms.DecimalField()
    eigenaar = forms.CharField()
    diernaam = forms.CharField()    
    totaal   = forms.DecimalField()

class DeliveryForm(forms.ModelForm):
    class Meta:
        model = Delivery
        fields = ['order', 'status', 'date', 'brief']

class NewPetForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = ['name', 'weight', 'ras', 'profile']

class PetForm(forms.ModelForm):
    checked_tastes = forms.CharField(max_length=1024, widget=forms.HiddenInput, required=False)

    class Meta:
        model = Pet
        fields = ['name', 'weight', 'ras', 'owner', 'profile', 'checked_tastes']
