from django.db import models
from django.db.models.signals import post_save

# Extern apps
from PIL import Image

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
    stock = models.PositiveIntegerField(default=0)

    objects = LibroManager()

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name='Libro'
        verbose_name_plural='Libros'
        ordering = ['titulo', 'fecha']
    
def optimize_image(sender, instance, **kwargs):
    if instance.portada:
        portada = Image.open(instance.portada.path)
        portada.save(instance.portada.path, quality=20, optimize=True)

post_save.connect(optimize_image, sender=Libro)