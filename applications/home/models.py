from django.db import models

# Create your models here.
class Persona(models.Model):
    '''Model definicion persona'''

    full_name = models.CharField('nombres', max_length=50, default='nombre-default')
    pais = models.CharField('Pais', max_length=30)
    pasaporte = models.CharField('Pasaporte', max_length=50)
    edad = models.PositiveIntegerField(default='18')
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
        abstract = True # Para no crearlo en la base de datos, solo sirve para heredar

class Empleados(Persona):
    empleo = models.CharField('Empleo', max_length=20)


    class Meta:
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'

class Cliente(Persona):
    email = models.EmailField('Email', max_length=254)


    class Meta:
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'