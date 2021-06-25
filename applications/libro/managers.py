from django.db import models

from django.db.models import Q, Count

# Django trigers
from django.contrib.postgres.search import TrigramSimilarity

# datetime para validar fechas recibidas por el html
import datetime

class LibroManager(models.Manager):
    ''' managers para el modelo libro '''

    def listar_libros(self, kword):
        result = self.filter(
            titulo__icontains=kword,
            fecha__range=('2020-06-01', '2022-01-01')
        )
        return result

    def listar_libros_trg(self, kword):
        if kword:
            result = self.filter(
                titulo__trigram_similar=kword,
            )
        else:
            result = self.all()[:10]
        return result

    def listar_libros_date(self, kword, fecha1, fecha2):

        date1 = datetime.datetime.strptime(fecha1, '%Y-%m-%d').date() # Mayus para valor de 4 cifras / minus para 2 cifras
        date2 = datetime.datetime.strptime(fecha2, '%Y-%m-%d').date()

        result = self.filter(
            titulo__icontains=kword,
            fecha__range=(date1, date2)
        )
        return result

    def listar_libros_categoria(self, categoria):

        return self.filter(
            categoria__id = categoria
        ).order_by('titulo')

    def add_autor_libro(self, libro_id, autor):
        libro = self.get(id=libro_id)
        libro.autores.add(autor)
        return libro

    def remove_autor_libro(self, libro_id, autor):
        libro = self.get(id=libro_id)
        libro.autores.remove(autor)
        return libro

    def libros_num_prestamos(self):
        return self.aggregate(
            num_prestamos=Count('libro_prestamo')
        )

    def num_libros_prestados(self):
        result = self.annotate(
            num_prestados=Count('libro_prestamo')
        )

        for r in result:
            print(r, r.num_prestados)

        return result


class CategoriaLibroManager(models.Manager):
    ''' managers para el modelo categoriaLibro '''

    def categoria_por_autor(self, autor):
        return self.filter(
            categoria_libro__autores__id=autor
        ).distinct()

    def listar_categorias_libro(self):
        result = self.annotate(
            num_libros=Count('categoria_libro')
        )

        # for r in result:
        #     print(r, r.num_libros)
        return result