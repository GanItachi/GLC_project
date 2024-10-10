from django.db import models

# Create your models here.
from django.db import models

class Cours(models.Model):
    titre = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.titre

class Ressource(models.Model):
    cours = models.ForeignKey(Cours, related_name='ressources', on_delete=models.CASCADE)
    titre = models.CharField(max_length=200)
    fichier = models.FileField(upload_to='ressources/')
    type = models.CharField(max_length=100, choices=(('pdf', 'PDF'), ('note', 'Note'), ('td', 'TD')))

    def __str__(self):
        return self.titre
