from django.shortcuts import render
from .models import Cours

def cours_list(request):
    cours_list = Cours.objects.prefetch_related('ressources').all()  # Récupère les cours et leurs ressources
    return render(request, 'cours_list.html', {'cours_list': cours_list})
