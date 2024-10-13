
from django.shortcuts import render, get_object_or_404
from Cours.models import Cours
from django.shortcuts import render, redirect
from django.forms import ModelForm, PasswordInput
from .models import Etudiants
from django import forms
from django.contrib.auth.hashers import make_password
from django.shortcuts import render, get_object_or_404


def Etudiant(request):
    cours = Cours.objects.all()  # Récupère tous les cours de la base de données
    return render(request, 'Vue_Etudiant.html', {'cours': cours})

def liste_cours(request):
    email = request.session.get('etudiant_email')  # Récupère l'email de la session
    etudiant = Etudiants.objects.get(email=email)  # Récupère l'étudiant correspondant à l'email
    cours = Cours.objects.all()  # Récupère tous les cours de la base de données
    return render(request, 'Vue_Etudiants_cours.html', {'cours': cours, 'etudiant': etudiant})


from django.shortcuts import render


def b_etudiant(request):
    email = request.session.get('etudiant_email')
    etudiant = Etudiants.objects.get(email=email)
    return render(request, 'Vue_Etudiant.html', {'etudiant': etudiant})

def profil_etudiant(request):
    email = request.session.get('etudiant_email')
    etudiant = Etudiants.objects.get(email=email)
    return render(request, 'profil_Etudiant.html', {'etudiant': etudiant})

# Create your views here.
class EtudiantForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Etudiants
        fields = ['nom','prenom','email','password', 'photo']

def register(request):
    if request.method == 'POST':
        form = EtudiantForm(request.POST, request.FILES)
        if form.is_valid():
            etudiant=form.save(commit=False)
            etudiant.password = form.cleaned_data['password']
            etudiant.save()
            return render(request, 'success.html')
    else:
        form = EtudiantForm()

    return render(request, 'register.html', {'form': form})

def success(request):
    return render(request, 'success.html')

def home(request) :
    return render (request, 'Acceuil.html')

