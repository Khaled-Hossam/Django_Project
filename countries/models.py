from django.db import models
from .models import *


class Country(models.Model):
    name = models.CharField(max_length=50)
    image = models.CharField(max_length=100)
    rate = models.IntegerField()
    description = models.TextField()


class City(models.Model):
    name = models.CharField(max_length=50)
    image = models.CharField(max_length=100)
    rate = models.IntegerField()
    description = models.TextField()
    country = models.ForeignKey(Country)


class Sight(models.Model):
    name = models.CharField(max_length=50)
    country = models.ForeignKey(City)
