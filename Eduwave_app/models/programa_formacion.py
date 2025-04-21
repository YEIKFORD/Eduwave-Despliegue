from django.db import models
from .red import Red

class ProgramaFormacion(models.Model):
    MODALIDAD = [
        ('V', 'Virtual'),
        ('P', 'Presencial'),
    ]
    modalidad = models.CharField(max_length=1, choices=MODALIDAD, default='P')
    nombre = models.CharField(max_length=50, unique=True, null=False)
    red = models.ForeignKey(Red, on_delete=models.PROTECT)
    def __str__(self):
        return self.nombre