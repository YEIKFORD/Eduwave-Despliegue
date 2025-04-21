from django.db import models
from .programa_formacion import ProgramaFormacion

class Ficha(models.Model):
    num_ficha = models.CharField(max_length=45, unique=True, null=False)
    programa = models.ForeignKey(ProgramaFormacion ,on_delete=models.PROTECT)
    def __str__(self):
        return self.num_ficha