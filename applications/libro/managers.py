from django.db import models

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

    def listar_libros_date(self, kword, fecha1, fecha2):

        date1 = datetime.datetime.strptime(fecha1, '%Y-%m-%d').date() # Mayus para valor de 4 cifras / minus para 2 cifras
        date2 = datetime.datetime.strptime(fecha2, '%Y-%m-%d').date()

        result = self.filter(
            titulo__icontains=kword,
            fecha__range=(date1, date2)
        )
        return result