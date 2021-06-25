from django.db import models

# Create your models here.
class Persona(models.Model):
    '''Model definicion persona'''

    full_name = models.CharField('nombres', max_length=50)
    pais = models.CharField('Pais', max_length=30)
    pasaporte = models.CharField('Pasaporte', max_length=50)
    edad = models.PositiveIntegerField()
    nickname = models.CharField('Usuario', max_length=10)

    def __str__(self):
        return self.full_name
    

    class Meta:
        verbose_name = 'Persona'
        verbose_name_plural = 'Personas'
        db_table = 'persona'
        unique_together = ['pais','nickname'] #bloquear que no se vuelva a repetir esta combinacion
        constraints = [ #restricciones
            models.CheckConstraint(check=models.Q(edad__gte=18), name='edad_mayor_18')
        ]