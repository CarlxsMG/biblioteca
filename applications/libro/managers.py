from django.db import models

class LibroManager(models.Manager):
    ''' managers para el modelo libro '''

    def listar_libros(self):
        return self.all()