from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('lectores/', views.ListLectores.as_view(), name='lectores'),
    path('prestamo-add/', views.AddPrestamo.as_view(), name='prestamo-add'),
    path('prestamo-multi/', views.AddMultiplePrestamo.as_view(), name='prestamo-multi'),
]