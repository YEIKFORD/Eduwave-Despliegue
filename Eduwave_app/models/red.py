from django.db import models
from .centro_formacion import CentroFormacion
    
class Red(models.Model):
    nombre = models.CharField(max_length=50, unique=True, null=False)
    centro_formacion = models.ForeignKey(CentroFormacion, on_delete=models.PROTECT)
    def __str__(self):
        return self.nombre