from django.urls import path
from . import views

urlpatterns = [
    path('',views.Etudiant,name='EtudiantA'),
    path('Cours',views.liste_cours,name='LISTE'),
]