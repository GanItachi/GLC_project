from django.db import models
from django import forms
from django.contrib.auth.models import User

# Create your models here.
from django.db import models

class Etudiants(models.Model):
    nom = models.CharField(max_length=20)
    prenom = models.CharField(max_length=20)
    email = models.EmailField(primary_key=True, unique=True)
    password = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='photos/', blank = True, null =True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nom', 'prenom', 'email']

    def __str__(self):
        return f"{self.prenom} {self.nom}"

