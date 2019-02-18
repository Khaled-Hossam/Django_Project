from django.shortcuts import render
from cities_light.models import Country

def index(request):
    countries = Country.objects.all()
    top6_countries = countries[0:6]
    print(top6_countries)
    context = {'countries': countries, 'top6_countries': top6_countries}
    return render(request, 'index.html', context)


def display(request, country_id):
    print(country_id)
    country = Country.objects.get(id = country_id)
    countries = Country.objects.all()
    context = {'country': country, 'countries': countries}
    return render(request, 'country.html', context)
