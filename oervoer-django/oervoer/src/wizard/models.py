from django.db import models
from django.db.models.fields import IntegerField

# Create your models here.

class Globals(models.Model):
    KAT = 'KAT'
    HOND = 'HOND'
    HEAD = 'KOP'
    DESC = models.CharField(max_length=50)
    MEALFACTOR  = models.FloatField (default=4.0) # included products that are bigger than meal size by this factor
    MEALFACTOR2 = models.FloatField (default=0.2) # included products smaller than meal size by this factor
    MEALFACTOR3 = models.FloatField (default=1.5)
    CATFACTOR   = models.FloatField (default=0.035) # 0.035 # 35 gram / kg / day
    DOGFACTOR   = models.FloatField (default=0.025) #0.025 # 25 gram / kg / day
    
    tries       = models.IntegerField(default=20) # 10
    LIKEFACTOR  = models.FloatField (default=4.0) #4.0 # sets the selection likelihood to be times this factor.
    SMALLMEAL   = models.IntegerField(default = 250) #250
    BIGMEAL     = models.IntegerField(default = 500) #500
    
    TESTENV     = models.CharField(max_length=50) #'OERVOERTESTENV'
    LEVERDEEL   = models.FloatField(default=0.4)
    VISFACTOR   = models.FloatField(default=0.15)
    PENSFACTOR  = models.FloatField(default=0.15)
    KARKASFACTOR = models.FloatField(default=0.7*0.5)
    ORGAANFACTOR = models.FloatField(default=0.7*0.5*0.15)
    SPIERFACTOR  = models.FloatField(default=0.7*0.5*0.4)
    BOTFACTOR = models.FloatField(default=0.7*0.5*0.45)
    REPEATS   = models.IntegerField(default=150)
    MEAL      = models.IntegerField(default=500)
    
    def get_factor(self, kathond):
        return  {Globals.KAT:self.CATFACTOR, Globals.HOND:self.DOGFACTOR}[kathond]
    def __unicode__(self):
        return self.DESC
    
class Package(models.Model):
    id = IntegerField(primary_key=True)
    choices = (('COMBI','COMBI'),
               ('100',  '100%'),
               ('PLUS', 'PLUS+'))
    type = models.CharField(max_length=10, choices=choices)
    def __unicode__(self):
        return self.type
    
class Ras(models.Model):
    choices = ((Globals.KAT,Globals.KAT), (Globals.HOND,Globals.HOND))
    ras = models.CharField(max_length=10, choices=choices)

    def __unicode__(self):
        return self.ras
    
class Owner(models.Model):
    id = IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    
    def __unicode__(self):
        return self.name

class Pet(models.Model):
    name = models.CharField(max_length=50)
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    ras = models.ForeignKey(Ras)
    owner= models.ForeignKey(Owner)
    factor = models.FloatField(default=1.0)
    profile = models.ForeignKey(Globals)

    def __unicode__(self):
        return self.name

    def is_kat(self):
        return self.ras.ras == 'KAT'
    
    def is_hond(self):
        return self.ras.ras == 'HOND'
    
    def get_meal_size(self):        
        return float(self.weight) * self.factor * self.profile.get_factor(self.ras.ras) / 2
    
    
class Order(models.Model):
    STATUS=(('pending','Pending'),
            ('completed','Completed'),
            ('processing','Processing'))
    id = IntegerField(primary_key=True)
    owner = models.ForeignKey(Owner)
    pet   = models.ForeignKey(Pet)
    package = models.ForeignKey(Package)
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    date = models.DateField()
    status = models.CharField(max_length=10, choices = STATUS)

    def __unicode__(self):
        return 'order {0}-{1}-{2}'.format(self.package,self.owner,self.pet)

    
class Taste(models.Model):
    id = IntegerField(primary_key=True)
    taste = models.CharField(max_length=30)
    is_big = models.BooleanField(default=False)
    is_small = models.BooleanField(default=False)
    is_fish = models.BooleanField(default=False)
    is_organ = models.BooleanField(default=False)
    is_fowl = models.BooleanField(default=False)
    is_else = models.BooleanField(default=False)
    is_liver = models.BooleanField(default=False)
    is_fishhead = models.BooleanField(default=False)

    def __unicode__(self):
        return self.taste
    
class MeatType(models.Model):
    id = IntegerField(primary_key=True)
    meat_type = models.CharField(max_length=30)
    is_fish = models.BooleanField(default=False)
    is_pens = models.BooleanField(default=False)
    is_spier = models.BooleanField(default=False)
    is_orgaan = models.BooleanField(default=False)
    is_karkas = models.BooleanField(default=False)
    is_bot = models.BooleanField(default=False)
    is_gemalen = models.BooleanField(default=False)

    def __unicode__(self):
        return self.meat_type
    
    def is_deelbaar(self):
        return self.is_bot() or self.is_pens() or self.is_spier() or self.is_orgaan() or self.is_gemalen()
        #VLEES_DEELBAAR = [BOT, ZACHTBOT, MIDDELBOT, HARDBOT, GEMALEN, VISGEMALEN, ORGAAN, PENS, SPIER]

    def is_portietype(self):
        return self.is_spier() or self.is_pens() or self.meat_type in ('GEMALEN', 'GEMALEN VIS') 

    
class prefers(models.Model):
    pet=models.ForeignKey(Pet)
    taste=models.ForeignKey(Taste)
    
    def __unicode__(self):
        return '{0} houdt van {1}'.format(self.pet,self.taste)
    

class Donts(models.Model):
    pet=models.ForeignKey(Pet)
    taste=models.ForeignKey(Taste)

    def __unicode__(self):
        return '{0} is allergisch voor {1}'.format(self.pet,self.taste)
    
class Product(models.Model):
    #{'id','name','sku','qty','smaak','vlees','shelf','weight', 'verpakking', kat_hond})

    id = IntegerField(primary_key=True)
    SHELVES = (('BINNENCELL','Binnencell'),
               ('BUITENCELL','Buitencell'),
               ('ORGAANBANK','OrgaanBank'),
               ('PARIS','Paris'))
    KATHOND = (('KAT','KAT'),
             ('HOND','HOND'),
             ('KAT&HOND','Beide'))
    name  = models.CharField(max_length=50)
    sku   = models.CharField(max_length=20)
    qty   = models.IntegerField()
    smaak = models.ForeignKey(Taste)
    vlees = models.ForeignKey(MeatType)
    shelf = models.CharField(max_length=20, choices=SHELVES)
    weight = models.DecimalField(max_digits=10, decimal_places=3)
    verpakking = models.IntegerField(default=1)
    kat_hond = models.CharField(max_length=10, choices=KATHOND)
    def __unicode__(self):
        return self.name
    
    def get_norm_weight(self):
        if self.verpakking == 0:
            self.verpakking = 1
        return self.weight/self.verpakking

    def get_kathond(self, kathond):
        
        return kathond == 'Beide' or kathond in self.kat_hond
    
class Delivery(models.Model):
    STATUS = (('PRE','PRE'),
              ('DELIVERED','DELIVERED'))
    order = models.ForeignKey(Order)
    status = models.CharField(max_length=10, choices=STATUS)
    date = models.DateField()
    brief = models.TextField()
    def __unicode__(self):
        return str(self.order)

class PickList(models.Model):
    delivery  = models.ForeignKey(Delivery)
    product = models.ForeignKey(Product)
    number = models.IntegerField(default=1)
    
    def __unicode__(self):
        return str('{}-{}x{}'.format(str(self.delivery),str(self.number),str(self.product)))
    