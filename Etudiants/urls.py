from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.b_etudiant,name='EtudiantA'),
    path('Cours',views.liste_cours,name='LISTE'),
    path('profil', views.profil_etudiant, name='profil_etudiant'),
    path('register', views.register, name='register'),
    path('success/', views.success, name='success'),
]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

