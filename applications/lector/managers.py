from django.db import models

class LectorManager(models.Manager):
    ''' managers para el modelo lector '''

    def listar_lectores(self):
        return self.all()