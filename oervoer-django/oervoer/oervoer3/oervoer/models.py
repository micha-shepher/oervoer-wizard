from django.db import models
from django.db.models.fields import IntegerField
from . import logger


# Create your models here.

class Globals(models.Model):
    KAT = 'KAT'
    HOND = 'HOND'
    HEAD = 'KOP'
    DESC = models.CharField(max_length=50)
    MEALFACTOR = models.FloatField(default=4.0, verbose_name='deelbaar factor1',
                                   help_text='<strong>Deelbare</strong> producten <strong>groter</strong> dan factor*maaltijd worden niet geselecteerd.')  # included products that are bigger than meal size by this factor
    MEALFACTOR2 = models.FloatField(default=0.2, verbose_name='deelbaar factor2',
                                    help_text='<strong>Deelbare</strong> producten <strong>kleiner</strong> dan factor*maaltijd worden niet geselecteerd.')  # included products smaller than meal size by this factor
    MEALFACTOR3 = models.FloatField(default=1.5, verbose_name='ondeelbaar factor1',
                                    help_text='<strong>Ondeelbare</strong> producten <strong>groter</strong> dan factor*maaltijd worden niet geselecteerd.')
    CATFACTOR = models.FloatField(default=0.035,
                                  help_text='Voor een kat, factor*kilo gewicht/#maaltijden = maaltijd')  # 0.035 # 35 gram / kg / day
    DOGFACTOR = models.FloatField(default=0.025,
                                  help_text='Voor een hond, factor*kilo gewicht/#maaltijden = maaltijd')  # 0.025 # 25 gram / kg / day
    tries = models.IntegerField(default=20)  # 10
    LIKEFACTOR = models.FloatField(
        default=4.0)  # 4.0 # sets the selection likelihood to be times this factor.
    SMALLMEAL = models.IntegerField(default=250,
                                    help_text='Bepaalt normale kleinportie groote')  # 250
    BIGMEAL = models.IntegerField(default=500,
                                  help_text='Bepaalt normale grootportie groote')  # 500
    TESTENV = models.CharField(max_length=50, default='')  # 'OERVOERTESTENV'
    LEVERDEEL = models.FloatField(default=0.4,
                                  help_text='Deel van lever in <strong>orgaan</strong>groep.')
    VISFACTOR = models.FloatField(default=0.15,
                                  help_text='Deel van VIS in totaal menu.')
    PENSFACTOR = models.FloatField(default=0.15,
                                   help_text='Deel van PENS in totaal menu.')
    KARKASFACTOR = models.FloatField(default=0.7 * 0.5,
                                     help_text='Deel van KARKAS in totaal menu.')
    ORGAANFACTOR = models.FloatField(default=0.7 * 0.5 * 0.15,
                                     help_text='Deel van ORGAAN in <strong>overgeblevende stuk</strong><p>Orgaan+Spier+Bot=1.0.')
    SPIERFACTOR = models.FloatField(default=0.7 * 0.5 * 0.4,
                                    help_text='Deel van SPIER in <strong>overgeblevende stuk</strong><p>Orgaan+Spier+Bot=1.0.')
    BOTFACTOR = models.FloatField(default=0.7 * 0.5 * 0.45,
                                  help_text='Deel van BOT in <strong>overgeblevende stuk</strong><p>Orgaan+Spier+Bot=1.0.')
    REPEATS = models.IntegerField(default=150,
                                  help_text="Aantal gegenereerde menu's waarvan de beste is gekozen.")
    MEAL = models.IntegerField(default=500, verbose_name='Maaltijdgrootte voor gemalen',
                               help_text='Verschil tussen deze en BIGMEAL of SMALLMEAL bepaalt de geprefereede portiegroote.')
    NRMEALS = models.IntegerField(default=2, verbose_name='aantal maaltijden')

    def get_factor(self, kathond):
        return {Globals.KAT: self.CATFACTOR, Globals.HOND: self.DOGFACTOR}[kathond]

    def __str__(self):
        return self.DESC


class Package(models.Model):
    id = IntegerField(primary_key=True)
    choices = (('COMBI', 'COMBI'),
               ('100', '100%'),
               ('PLUS', 'PLUS+'))
    type = models.CharField(max_length=10, choices=choices)

    def __str__(self):
        return self.type


class Ras(models.Model):
    choices = ((Globals.KAT, Globals.KAT), (Globals.HOND, Globals.HOND))
    ras = models.CharField(max_length=10, choices=choices)

    def __str__(self):
        return self.ras


class Owner(models.Model):
    id = IntegerField(primary_key=True)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Pet(models.Model):
    name = models.CharField(max_length=50)
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    ras = models.ForeignKey(Ras, on_delete=models.CASCADE)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    factor = models.FloatField(default=1.0)
    birthdate = models.DateField(default='1999-01-01')
    profile = models.ForeignKey(Globals, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def is_kat(self):
        return self.ras.ras == 'KAT'

    def is_hond(self):
        return self.ras.ras == 'HOND'

    def get_meal_size(self):
        logger.info(f"getmeal sized{self.weight}, {self.is_hond()},"
                    f" {self.profile.NRMEALS}")
        return float(self.weight) * self.factor * self.profile.get_factor(
            self.ras.ras) / self.profile.NRMEALS


class Order(models.Model):
    STATUS = (('pending', 'Pending'),
              ('completed', 'Completed'),
              ('processing', 'Processing'))
    id = IntegerField(primary_key=True)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    package = models.ForeignKey(Package, on_delete=models.CASCADE)
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    date = models.DateField()
    status = models.CharField(max_length=10, choices=STATUS)
    newpet = models.BooleanField(default=False)

    def __str__(self):
        return 'order {0}-{1}-{2}'.format(self.package, self.owner, self.pet)


class Comment(models.Model):
    when = models.DateTimeField()
    what = models.CharField(max_length=20)
    desc = models.CharField(max_length=512)
    weight = models.DecimalField(max_digits=5, decimal_places=2, default=0, null=True)
    order = models.ForeignKey(Order, blank=True, null=True, on_delete=models.CASCADE)
    desc2 = models.CharField(max_length=512)


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

    def __str__(self):
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

    def __str__(self):
        return self.meat_type

    def is_deelbaar(self):
        return self.is_bot or self.is_pens or self.is_spier or self.is_orgaan or self.is_gemalen
        # VLEES_DEELBAAR = [BOT, ZACHTBOT, MIDDELBOT, HARDBOT, GEMALEN, VISGEMALEN, ORGAAN, PENS, SPIER]

    def is_portietype(self):
        return self.is_spier or self.is_pens or self.meat_type in (
        'GEMALEN', 'GEMALEN VIS')


class prefers(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    taste = models.ForeignKey(Taste, on_delete=models.CASCADE)

    def __str__(self):
        return '{0} houdt van {1}'.format(self.pet, self.taste)


class Donts(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    taste = models.ForeignKey(Taste, on_delete=models.CASCADE)

    def __str__(self):
        return '{0} is allergisch voor {1}'.format(self.pet, self.taste)


class Product(models.Model):
    # {'id','name','sku','qty','smaak','vlees','shelf','weight', 'verpakking', kat_hond})

    id = IntegerField(primary_key=True)
    SHELVES = (('BINNENCELL', 'Binnencell'),
               ('BUITENCELL', 'Buitencell'),
               ('ORGAANBANK', 'OrgaanBank'),
               ('PARIS', 'Paris'))
    KATHOND = (('KAT', 'KAT'),
               ('HOND', 'HOND'),
               ('KAT&HOND', 'Beide'))
    name = models.CharField(max_length=50)
    sku = models.CharField(max_length=20)
    qty = models.IntegerField()
    smaak = models.ForeignKey(Taste, on_delete=models.CASCADE)
    vlees = models.ForeignKey(MeatType, on_delete=models.CASCADE)
    shelf = models.CharField(max_length=20, choices=SHELVES)
    weight = models.DecimalField(max_digits=10, decimal_places=3)
    verpakking = models.IntegerField(default=1)
    kat_hond = models.CharField(max_length=10, choices=KATHOND)

    def __str__(self):
        return self.name

    def get_norm_weight(self):
        if self.verpakking == 0:
            self.verpakking = 1
        return self.weight / self.verpakking

    def get_kathond(self, kathond):
        return kathond == 'Beide' or kathond in self.kat_hond


class Delivery(models.Model):
    STATUS = (('PRE', 'PRE'),
              ('DELIVERED', 'DELIVERED'))
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=STATUS)
    date = models.DateField()
    brief = models.TextField()

    def __str__(self):
        return str(self.order)


class PickList(models.Model):
    delivery = models.ForeignKey(Delivery, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    number = models.IntegerField(default=1)

    class Meta:
        ordering = ['delivery__date']

    def __str__(self):
        return str(
            '{}-{}x{}'.format(str(self.delivery), str(self.number), str(self.product)))
