
from django.shortcuts import render, get_object_or_404
from Cours.models import Cours

def Etudiant(request):
    cours = Cours.objects.all()  # Récupère tous les cours de la base de données
    return render(request, 'Vue_Etudiant.html', {'cours': cours})

def liste_cours(request):
    cours = Cours.objects.all()  # Récupère tous les cours de la base de données
    return render(request, 'Vue_Etudiants_cours.html', {'cours': cours})

from django.shortcuts import render
from .models import Etudiant

def b_etudiant(request, etudiant_id):
    etudiant = get_object_or_404(Etudiant, id=etudiant_id)
    context = {'etudiant': etudiant}  # Préparer les données pour les passer au template
    return render(request, 'Vue_Etudiant.html', context)

# views.py
from django.shortcuts import render, get_object_or_404
from .models import Etudiant

def profil_etudiant(request, etudiant_id):
    etudiant = get_object_or_404(Etudiant, id=etudiant_id)  # Récupère l'étudiant par ID
    return render(request, 'profil_Etudiant.html', {'etudiant': etudiant})

