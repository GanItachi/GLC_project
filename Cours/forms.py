# forms.py
from django import forms
from .models import Ressource

class RessourceForm(forms.ModelForm):
    class Meta:
        model = Ressource
        fields = ['titre', 'fichier', 'type', 'description', 'illustration']
