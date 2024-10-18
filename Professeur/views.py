from .models import Professeurs
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404, render
from Cours.models import Cours
from Cours.models import Ressource
from Cours.forms import RessourceForm

# Create your views here.
def profil_Professeur(request):
    email = request.session.get('Professeur_email')
    Professeur = Professeurs.objects.get(email=email)
    return render(request, 'profil_Professeur.html', {'Professeur': Professeur})




def cours_professeur(request):
    email = request.session.get('Professeur_email')
    idP = request.session.get('Professeur_id')
    professeur = Professeurs.objects.get(id= idP)
    cours = Cours.objects.filter(professeur=professeur) # Récupère les cours attribués au professeur
    return render(request, 'Vue_professeur_cours.html', {'cours': cours})

def detail_cours(request, id):
    email = request.session.get('Professeur_email')
    Professeur = Professeurs.objects.get(email=email)
    cours = get_object_or_404(Cours, id= id)
    ressources = Ressource.objects.filter(cours=cours)  # Récupère les ressources liées à ce cours
    
    # Formulaire pour ajouter des ressources
    if request.method == 'POST':
        form = RessourceForm(request.POST, request.FILES)
        if form.is_valid():
            ressource = form.save(commit=False)
            ressource.cours = cours  # Associe la ressource au cours
            ressource.save()
            return redirect('details', id=cours.id)
    else:
        form = RessourceForm()

    return render(request, 'detail_cours.html', {
        'cours': cours,
        'ressources': ressources,
        'form': form,
        'Professeur': Professeur, 
    })
    
    
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages

def supprimer_ressource(request, ressource_id):
    if request.method == "POST":
        ressource = get_object_or_404(Ressource, id=ressource_id)
        ressource.delete()
        messages.success(request, "La ressource a été supprimée avec succès.")
        return redirect('details', id=ressource.cours.id)  # Redirige vers la page du cours après la suppression
    
def logout_professeur(request):
    request.session.flush()  # Supprime toutes les données de la session
    return redirect('accueil')

