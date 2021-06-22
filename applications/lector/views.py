from django.shortcuts import render

from django.views.generic import ListView

# Local models
from .models import Lector

# Create your views here.
class ListLectores(ListView):
    template_name = 'lector/lista.html'
    context_object_name = 'lista_lectores'

    def get_queryset(self):
        return Lector.objects.listar_lectores()