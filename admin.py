from django.contrib import admin
from .models import Country

class CountryAdmin(admin.ModelAdmin):
    list_display = ['name', 'capital', 'area', 'population']

admin.site.register(Country, Country

