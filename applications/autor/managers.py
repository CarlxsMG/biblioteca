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

    def buscar_autores_excl_edad(self, kword):

        result = self.filter(
            Q(nombre__icontains=kword) |
            Q(apellidos__icontains=kword)
            ).exclude(
                Q(edad=45) |
                Q(edad=20)
                )

        return result

    def buscar_autores_filter_edad(self, kword):

        result = self.filter(
            Q(nombre__icontains=kword) |
            Q(apellidos__icontains=kword)
            ).filter(
                Q(edad=45) |
                Q(edad=20)
                )

        return result
    
    def buscar_autores_edad_mayorQue(self, kword):

        result = self.filter(
            edad__gt=40,
            edad__lt=80,
            ).order_by(
                '-apellidos', # al reves
                'nombre',
                'id'
            )

        return result