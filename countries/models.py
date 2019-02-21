from django.db import models
from .models import *


class Country(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='uploads/countries/', max_length=200)
    rate = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Countries"


class City(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='uploads/cities/', max_length=200)
    rate = models.IntegerField()
    description = models.TextField()
    latitude = models.DecimalField(max_digits=8, decimal_places=5)
    longitude = models.DecimalField(max_digits=8, decimal_places=5)
    country = models.ForeignKey(Country)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Cties"


class Sight(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='uploads/sights/', max_length=200, default=None)
    description = models.TextField(default=None)
    city = models.ForeignKey(City)

    def __str__(self):
        return self.name

class Hotel(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='uploads/sights/', max_length=200, default=None)
    city = models.ForeignKey(City, default=None)
    
