from django.shortcuts import render
# from cities_light.models import Country, City
from .models import *

def index(request):
    countries = Country.objects.all()
    top6_countries = countries[0:6]
    top6_cities = City.objects.all()[0:6]
    context = {'countries': countries, 'top6_countries': top6_countries, 'top6_cities': top6_cities}
    return render(request, 'index.html', context)


def display(request, country_id):
    print(country_id)
    country = Country.objects.get(id = country_id)
    countries = Country.objects.all()
    cities = City.objects.filter(country_id = country_id)
    context = {'country': country, 'countries': countries, 'cities': cities}
    return render(request, 'country.html', context)


def display_city(request, city_id):
    city = City.objects.get(id = city_id)
    countries = Country.objects.all()
    # sights = City.objects.filter(country_id = country_id)
    context = {'city': city, 'countries': countries}
    return render(request, 'city.html', context)

