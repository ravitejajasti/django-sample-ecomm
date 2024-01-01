from django.db import models
from django.conf import settings
from phonenumber_field.modelfields import PhoneNumberField

class Country(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Country'
        verbose_name_plural = 'Countries'

class State(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Company(models.Model):
    company_status_choices= {
    "ACT": "ACTIVE",
    "DRM": "DORMANT",
    "INAC": "INACTIVE",
    "DRFT": "DRAFT"
    }

    company_types = {
        'PVT': 'Private Limited',
        'LTD': 'Public Limited',
        'SLP': 'Sole Proprietorship',
        'None': 'Unknown'
    }
    name = models.CharField(max_length=200)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Owner')
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True, verbose_name='Country')
    state = models.ForeignKey(State, on_delete=models.SET_NULL, null=True, verbose_name='State')
    cin = models.CharField(max_length=30, default=None, null=True, verbose_name='CIN')
    status = models.CharField(max_length=15, choices=company_status_choices, default='DRAFT', verbose_name='Status')
    address = models.CharField(max_length=40, default=None, null=True, verbose_name='Address')
    zip = models.CharField(max_length=6, default=None, null=True, blank=True, verbose_name='Zip Code')
    type = models.CharField(max_length=4, choices=company_types, default=company_types["None"], verbose_name='Company Type')
    tan = models.CharField(max_length=30, default=None, null=True, blank=True, verbose_name='TAN #')
    pan = models.CharField(max_length=10, default=None, null=True, blank=True, verbose_name= 'PAN #')
    gstin = models.CharField(max_length=20, default=None, null=True, blank=True, verbose_name= 'GSTIN')
    email = models.EmailField(max_length=254, null=True, default=None, blank=True, verbose_name= 'Company Email')
    phone = PhoneNumberField(null=True, blank=True, unique=True, name="Phone Number")
    
    # add more fields as per your requirements

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Company'
        verbose_name_plural = 'Companies'


class Director(models.Model):
    dir_status_choices= {
    "ACT": "ACTIVE",
    "INAC": "INACTIVE",
    "DRFT": "DRAFT"
    }
    name = models.CharField(max_length=200)
    #owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True, verbose_name='Country')
    state = models.ForeignKey(State, on_delete=models.SET_NULL, null=True, verbose_name='State')
    din = models.CharField(max_length=30, default=None, null=True, blank=True, verbose_name='DIN #')
    status = models.CharField(max_length=15, choices=dir_status_choices, default='DRAFT', verbose_name='Status')
    address = models.CharField(max_length=40, default=None, null=True, blank=True, verbose_name='Address')
    zip = models.CharField(max_length=6, default=None, null=True, blank=True, verbose_name='Zip Code')
    # add more fields as per your requirements
    pan = models.CharField(max_length=10, default=None, null=True, blank=True, verbose_name='PAN #')
    company = models.ManyToManyField(Company, through='CompanyDirector', verbose_name='Linked Companies')#on_delete=models.SET_NULL, null=True)
    email = models.EmailField(max_length=254, null=True, default=None, blank=True, verbose_name='Email')
    phone = PhoneNumberField(null=True, blank=True, unique=True, name="Phone Number")

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Director'
        verbose_name_plural = 'Directors'

class CompanyDirector(models.Model):

    company = models.ForeignKey(Company, on_delete=models.SET_NULL, null=True, verbose_name='Company')
    director = models.ForeignKey(Director, on_delete=models.SET_NULL, null=True, verbose_name='Director')
    class Meta:
        verbose_name = 'Associated with'
        verbose_name_plural = 'Associated with'



class OrderType(models.Model):
    def get_currencies():
        return {i: i for i in settings.CURRENCIES}
    type = models.CharField(max_length=200, verbose_name='Order Type')
    description = models.TextField(verbose_name='Description', help_text='Enter a brief description of the Order Type')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=3, choices=get_currencies)

    def __str__(self):
        return self.type

class Order(models.Model):
    order_status_choices = {
    "COMPLETED": "COMPLETED",
    "RENEWED": "RENEWED",
    "CANCELLED": "CANCELLED",
    "RECEIVED": "RECEIVED"

    }

    company = models.ForeignKey(Company, on_delete=models.SET_NULL, null=True, verbose_name='Company')
    status = models.CharField(max_length=15, choices=order_status_choices, default='RECEIVED', verbose_name='Status')
    type = models.ForeignKey(OrderType, on_delete=models.SET_NULL, null=True, default=None, verbose_name='Order Type')
    
    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'

