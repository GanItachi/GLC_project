
from django.shortcuts import render
from Cours.models import Cours

def Etudiant(request):
    cours = Cours.objects.all()  # Récupère tous les cours de la base de données
    return render(request, 'Vue_Etudiant.html', {'cours': cours})

def liste_cours(request):
    cours = Cours.objects.all()  # Récupère tous les cours de la base de données
    return render(request, 'Vue_Etudiants_cours.html', {'cours': cours})
