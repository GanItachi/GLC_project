
from django.shortcuts import render, redirect
from django.forms import ModelForm
from .models import loginP
from Professeur.models import Professeurs
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import check_password


# Create your views here.
class LoginForm(ModelForm):
    class Meta:
        model = loginP
        fields=['email','password']

def connecterP(request):
    if request.method == 'POST': 
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            try:
                Professeur = Professeurs.objects.get(email=email)
                # Vérification du mot de passe haché
                if Professeur.password==password:
                    # Si le mot de passe est correct, démarre la session utilisateur
                    request.session['Professeur_email'] = Professeur.email
                    request.session['Professeur_id'] = Professeur.id
                    return redirect('AccP')  # Page après connexion
                else:
                    messages.error(request, "Mot de passe incorrect")
            except Professeurs.DoesNotExist:
                messages.error(request, "Email non trouvé")
    else:
        form = LoginForm()
    
    return render(request, 'loginP.html', {'form': form})



def AccP(request) :
    email = request.session.get('Professeur_email')
    Professeur = Professeurs.objects.get(email=email)
    return render(request, 'Vue_Professeur.html', {'Professeur': Professeur})
