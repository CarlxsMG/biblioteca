from django.db import models

from django.db.models import Q

class AutorManager(models.Manager):
    ''' managers para el modelo autor '''

    def listar_autores(self):
        return self.all()

    def buscar_autores(self, kword):

        result = self.filter(
            Q(nombre__icontains=kword) |
            Q(apellidos__icontains=kword)
            )

        return result