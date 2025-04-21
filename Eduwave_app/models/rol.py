from django.db import models

class Rol(models.Model):
    codigo = models.CharField(max_length=10, unique=True, null=False)
    nombre = models.CharField(max_length=50, unique=True, null=False)
    descripcion = models.CharField(max_length=200, blank=False)
    def __str__(self):
        return self.nombre