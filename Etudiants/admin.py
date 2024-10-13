from django.contrib import admin
from .models import Etudiants # Assure-toi que Cours est bien dans l'application actuelle
from django.contrib.admin import AdminSite

# Register your models here.
admin.site.register(Etudiants)