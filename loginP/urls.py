from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns=[
    path('', views.connecterP, name='loginP'),
    path('admin/', views.connecterP, name='admin'),
    path('Professeur', views.AccP, name='AccP'),
]