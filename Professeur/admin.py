from django.contrib import admin
from .models import Professeurs

from django.contrib import admin
from django.utils.html import format_html
from .models import Professeurs


# Register your models here.
class ProfesseurAdmin(admin.ModelAdmin):
    list_display = ('nom', 'email', 'date_embauche', 'telephone', 'afficher_photo')

    def afficher_photo(self, obj):
        if obj.photo:
            return format_html('<img src="{}" style="height:130px;width:130px;border-radius:50%;"/>', obj.photo.url)
        return "Pas d'image"

    afficher_photo.short_description = "Photo"
    
admin.site.register(Professeurs, ProfesseurAdmin)