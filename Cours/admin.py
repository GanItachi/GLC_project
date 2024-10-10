
from django.contrib import admin
from .models import Cours
from .models import Ressource# Assure-toi que Cours est bien dans l'application actuelle
from django.contrib.admin import AdminSite

# Enregistre le modèle dans l'admin
admin.site.register(Cours)
admin.site.register(Ressource)


# Modification du site d'administration
admin.site.site_header = "ADMIN DOODLE ENSEA"
admin.site.site_title = "Gestion des utilisateurs"
admin.site.index_title = "Bienvenue sur le panneau d'administration"

