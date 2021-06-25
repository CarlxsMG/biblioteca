from django.db import models

# Local apps
from applications.autor.models import Autor

# Local managers
from .managers import LibroManager, CategoriaLibroManager

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=50)

    objects = CategoriaLibroManager()

    def __str__(self):
        return str(self.id) + ' - ' + self.nombre


class Libro(models.Model):
    categoria = models.ForeignKey(
        Categoria, 
        on_delete=models.CASCADE,
        related_name='categoria_libro')
    autores = models.ManyToManyField(Autor)
    titulo = models.CharField(max_length=50)
    fecha = models.DateField('Fecha lanzamiento')
    portada = models.ImageField(upload_to='portada', null=True, blank=True)
    visitas = models.PositiveIntegerField(default=0)

    objects = LibroManager()

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name='Libro'
        verbose_name_plural='Libros'
        ordering = ['titulo', 'fecha']
    