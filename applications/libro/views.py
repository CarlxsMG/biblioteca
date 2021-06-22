from django.shortcuts import render

from django.views.generic import ListView

# Local models
from .models import Libro

# Create your views here.
class ListLibros(ListView):
    template_name = 'libro/lista.html'
    context_object_name = 'lista_libros'

    def get_queryset(self):
        return Libro.objects.listar_libros()
