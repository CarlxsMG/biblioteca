from django.db import models
from django.db.models import Avg, Sum

class LectorManager(models.Manager):
    ''' managers para el modelo lector '''

    def listar_lectores(self):
        return self.all()


class PrestamoManager(models.Manager):
    ''' managers procedimiento para prestamo '''

    def libros_promedio_edades(self):
        result = self.filter(
            libro__id='5'
        ).aggregate(
            promedio_edad=Avg('lector__edad'),
            suma_edad=Sum('lector__edad'),
        )
        return result