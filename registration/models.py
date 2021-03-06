from django.db import models
from django_countries.fields import CountryField
from django.utils import timezone


# Create model: registration and contacts
class Registration(models.Model):

    def __str__(self):
        return self.login

    id = models.AutoField(primary_key=True)
    login = models.CharField('login:', max_length=32, unique=True)
    email = models.EmailField('email', max_length=32, unique=True,)
    password = models.CharField('password', max_length=32, null=True)
    repeat_password = models.CharField('repeat password', max_length=32)
    date_filed = models.DateField(default=timezone.now)


class Contact(models.Model):
    registration = models.ForeignKey(Registration)
    last_name = models.CharField('last name', max_length=32)
    first_name = models.CharField('first name', max_length=32)
    patronymic = models.CharField('patronymic', max_length=32)
    country = CountryField(blank_label='(select country)')
    city = models.CharField('city', max_length=32)
    street = models.CharField('street', max_length=32)
    house = models.IntegerField('house')
    house_fraction = models.IntegerField('fraction', blank=True, null=True)
    appartment = models.IntegerField('appartment')
    index = models.IntegerField('index')