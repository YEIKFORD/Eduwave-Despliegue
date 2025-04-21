from django.db import models

class TipoAmbiente(models.Model):
    nombre = models.CharField(max_length=300, null=False)
    descripcion = models.CharField(max_length=450, null=False)