from django.db import models
from .municipio import Municipio

class CentroFormacion(models.Model):
    codigo = models.CharField(max_length=10, unique=True, null=False)
    nombre = models.CharField(max_length=300, null=False)
    direccion = models.CharField(max_length=300, null=False)
    telefono = models.CharField(max_length=10, blank=True, null=True)
    municipio = models.ForeignKey(Municipio, on_delete=models.PROTECT)

    def __str__(self):
        return self.nombre
