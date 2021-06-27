from django.db import models

# Local managers
from .managers import LectorManager, PrestamoManager

# Local apps
from applications.libro.models import Libro
from applications.autor.models import Persona

# Create your models here.
class Lector(Persona):

    objects = LectorManager()

    class Meta:
        verbose_name = 'lector'
        verbose_name_plural = 'lectores'
    
class Prestamo(models.Model):
    lector = models.ForeignKey(Lector, on_delete=models.CASCADE)
    libro = models.ForeignKey(
        Libro, 
        on_delete=models.CASCADE, 
        related_name='libro_prestamo')
    fecha_prestamo = models.DateField()
    fecha_devolucion = models.DateField(blank=True, null=True)
    devuelto = models.BooleanField()

    objects = PrestamoManager()

    def save(self, *args, **kwargs):

        self.libro.stock -= 1

        self.libro.save()

        super(Prestamo, self).save(*args, **kwargs)

    def __str__(self):
        return self.libro.titulo
    