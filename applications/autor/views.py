from django.shortcuts import render

from django.views.generic import ListView

# Local models
from .models import Autor

# Create your views here.
class ListAutores(ListView):
    context_object_name = 'lista_autores'
    template_name = 'autor/lista.html'

    def get_queryset(self):
        return Autor.objects.listar_autores()