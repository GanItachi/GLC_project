
from django.shortcuts import render, redirect
from django.forms import ModelForm
from .models import Login
from Etudiants.models import Etudiants
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import check_password


# Create your views here.
class LoginForm(ModelForm):
    class Meta:
        model = Login
        fields=['email','password']

def connecter(request):
    if request.method == 'POST': 
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            try:
                etudiant = Etudiants.objects.get(email=email)
                # Vérification du mot de passe haché
                if etudiant.password==password:
                    # Si le mot de passe est correct, démarre la session utilisateur
                    request.session['etudiant_email'] = etudiant.email
                    return redirect('Acc')  # Page après connexion
                else:
                    messages.error(request, "Mot de passe incorrect")
            except Etudiants.DoesNotExist:
                messages.error(request, "Email non trouvé")
    else:
        form = LoginForm()
    
    return render(request, 'login.html', {'form': form})



def Acc(request) :
    email = request.session.get('etudiant_email')
    etudiant = Etudiants.objects.get(email=email)
    return render(request, 'Vue_Etudiant.html', {'etudiant': etudiant})