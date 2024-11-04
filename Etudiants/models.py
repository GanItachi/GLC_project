from django.db import models
from django import forms
from django.contrib.auth.models import User
from django.core.files import File
from django.conf import settings
import os

# Create your models here.
from django.db import models

class Etudiants(models.Model):
    NATIONALITES_CHOICES = [
        ('CI', 'Côte d\'Ivoire'),
        ('BF', 'Burkina Faso'),
        ('TG', 'Togo'),
        ('BJ', 'Bénin'),
        ('SN', 'Sénégal'),
        ('ML', 'Mali'),
        ('CM', 'Cameroun'),
        ('CM', 'Cameroun'),
        ('HA', 'Haïti'),
        ]
    nom = models.CharField(max_length=20)
    prenom = models.CharField(max_length=20)
    email = models.EmailField(primary_key=True, unique=True)
    password = models.CharField(max_length=50)
    nationalite = models.CharField(max_length=2, choices=NATIONALITES_CHOICES)
    photo = models.ImageField(upload_to='photos/', blank = True, null =True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nom', 'prenom', 'email']

    def __str__(self):
        return f"{self.prenom} {self.nom}"

    def save(self, *args, **kwargs):
        if not self.photo:
            default_image_path = os.path.join(settings.MEDIA_ROOT, 'default_images/pp_default.jpg')
            
            # Vérifie si le fichier existe
            if os.path.exists(default_image_path):
                # Ouvre le fichier et l'assigne à l'photo
                with open(default_image_path, 'rb') as f:
                    self.photo.save(os.path.basename(default_image_path), File(f), save=False)
            else:
                # Optionnel : log ou gérer le cas où l'image par défaut n'existe pas
                print(f"Le fichier {default_image_path} n'existe pas.")
        
        super().save(*args, **kwargs)

