from django.db import models
from .tipo_ambiente import TipoAmbiente
from .sede import Sede

class Ambiente(models.Model):
    ESTADO = [
        ('A', 'Apto'),
        ('N', 'No apto')
    ]
    numero_ambiente = models.CharField(max_length=100, unique=True, null=False)
    estado = models.CharField(max_length=1, choices=ESTADO, null=False, default='A')
    tipo_ambiente = models.ForeignKey(TipoAmbiente, on_delete=models.PROTECT)
    sede = models.ForeignKey(Sede, on_delete=models.PROTECT)

    def __str__(self):
        return self.numero_ambiente