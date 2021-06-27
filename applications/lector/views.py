#Local python modules
from datetime import date

from django.shortcuts import render

from django.views.generic import ListView
from django.views.generic.edit import FormView

# Local models
from .models import Lector
from .models import Prestamo
from .forms import PrestamoForm

# Create your views here.
class ListLectores(ListView):
    template_name = 'lector/lista.html'
    context_object_name = 'lista_lectores'

    def get_queryset(self):
        return Lector.objects.listar_lectores()

class RegistrarPrestamo(FormView):
    template_name = 'lector/add_prestamo.html'
    form_class = PrestamoForm
    success_url = '.' #para recargar la misma vista

    def form_valid(self, form):

        # Prestamo.objects.create(
        #     lector = form.cleaned_data['lector'],
        #     libro = form.cleaned_data['libro'],
        #     fecha_prestamo = date.today(),
        #     devuelto = False
        # )

        prestamo = Prestamo(
            
            lector = form.cleaned_data['lector'],
            libro = form.cleaned_data['libro'],
            fecha_prestamo = date.today(),
            devuelto = False
        )
        prestamo.save()

        return super(RegistrarPrestamo, self).form_valid(form)