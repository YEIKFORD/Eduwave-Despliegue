from django.db import models

class Regional(models.Model):
    codigo = models.CharField(max_length=2, unique=True, null=False)
    nombre = models.CharField(max_length=60, null=False)
    def __str__(self):
        return self.nombre   