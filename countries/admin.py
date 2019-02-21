from django.contrib import admin
from .models import *


class CustomInlineCity(admin.StackedInline):
    model = City
    extra = 2

class CustomCountry(admin.ModelAdmin):

    list_display = ('name', 'id')
    search_fields = ['name', 'id']
    # inlines = [CustomInlineCity]


class CustomSight(admin.ModelAdmin):

    list_display = ('name', 'id', 'city_id')
    search_fields = ['name', 'id']

admin.site.register(Country, CustomCountry)
admin.site.register(City)
admin.site.register(Sight, CustomSight)
admin.site.register(Hotel, CustomSight)

