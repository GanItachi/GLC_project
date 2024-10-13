from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns=[
    path('', views.connecter, name='login'),
    path('admin/', views.connecter, name='admin'),
    path('Etudiant', views.Acc, name='Acc'),
]



