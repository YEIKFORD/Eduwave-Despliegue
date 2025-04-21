from django.db import models
from .categoria import Categoria


class SubCategoria(models.Model):
    nombre = models.CharField(max_length=100, null=False)
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)
    def __str__(self):
        return self.nombre