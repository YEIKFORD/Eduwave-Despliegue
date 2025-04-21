from django.db import models
from .centro_formacion import CentroFormacion

class Sede(models.Model):
    codigo = models.CharField(max_length=100, unique=True, null=False)
    nombre = models.CharField(max_length=300, null=False)
    direccion = models.CharField(max_length=300, null=False)
    telefono = models.CharField(max_length=10, blank=True, null=True)
    centro_formacion = models.ForeignKey(CentroFormacion, on_delete=models.PROTECT)
    def __str__(self):
        return self.nombre 