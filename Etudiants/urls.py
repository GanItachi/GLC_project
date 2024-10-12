from django.urls import path
from . import views

urlpatterns = [
    path('<int:etudiant_id>',views.b_etudiant,name='EtudiantA'),
    path('Cours',views.liste_cours,name='LISTE'),
    path('etudiant/<int:etudiant_id>/', views.profil_etudiant, name='profil_etudiant')
]