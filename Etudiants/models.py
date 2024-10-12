from django.db import models

# Create your models here.
from django.db import models

class Etudiant(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    email = models.EmailField()
    Photos = models.FileField(upload_to='./photos/', blank=True, null=True)

    def __str__(self):
        return f"{self.prenom} {self.nom}"

