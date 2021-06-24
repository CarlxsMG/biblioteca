from django.shortcuts import render

from django.views.generic import ListView

# Local models
from .models import Libro

# Create your views here.
class ListLibros(ListView):
    template_name = 'libro/lista.html'
    context_object_name = 'lista_libros'

    def get_queryset(self):
        clave = self.request.GET.get('kword','')
        f1 = self.request.GET.get('fecha1','')
        f2 = self.request.GET.get('fecha2','')

        if f1 and f2:
            return Libro.objects.listar_libros_date(clave,f1,f2)
        else:
            return Libro.objects.listar_libros(clave)

        
