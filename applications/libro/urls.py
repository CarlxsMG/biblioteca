from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('libros/', views.ListLibros.as_view(), name='libros'),
    path('libros-categoria/', views.ListLibrosCategoria.as_view(), name='librosCategoria'),
]