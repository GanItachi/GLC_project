from django.contrib import admin
from .models import Etudiants # Assure-toi que Cours est bien dans l'application actuelle
from django.contrib.admin import AdminSite
from django.contrib import admin
from django.utils.html import format_html

class EtudiantsAdmin(admin.ModelAdmin):
    list_display = ('nom', 'email', 'afficher_photo')

    def afficher_photo(self, obj):
        if obj.photo:
            return format_html('<img src="{}" style="height:130px;width:130px;border-radius:50%;"/>', obj.photo.url)
        return "Pas d'image"

    afficher_photo.short_description = "Photo"
    
admin.site.register(Etudiants, EtudiantsAdmin)