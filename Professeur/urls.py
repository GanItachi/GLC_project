from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('Cours/',views.cours_professeur,name='coursP'),
    path('Details/<int:id>/',views.detail_cours,name='details'),
    path('profil', views.profil_Professeur, name='profil_Professeur'),
    path('Deconnexion', views.logout_professeur, name='logoutp'),
    path('cours/ressource/supprimer/<int:ressource_id>/', views.supprimer_ressource, name='supprimer_ressource'),
]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)