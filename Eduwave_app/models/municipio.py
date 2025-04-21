from django.db import models
from .regional import Regional


class Municipio(models.Model):
    codigo_DANE = models.CharField(max_length=20, unique=True, null=False )
    nombre =  models.CharField(max_length=50, null=False)
    regional = models.ForeignKey(Regional, on_delete=models.PROTECT)
    def __str__(self):
        return self.nombre   