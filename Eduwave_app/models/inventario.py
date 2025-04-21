from django.db import models
from .subcategoria import SubCategoria
from .ambiente import Ambiente




class Inventario(models.Model):
    ESTADO = [
        ('A', 'Apto'),
        ('N', 'No apto')
    ]
    codigo = models.CharField(max_length=40, unique=True, null=False )
    nombre = models.CharField(max_length=100, null=False)
    descripcion = models.CharField(max_length=100, null=False)
    fecha_adquisicion = models.DateField(null=False)
    num_placa_almacen = models.CharField(max_length=45, null=False)
    precio_compra = models.DecimalField(max_digits=20, decimal_places=2, null=False)
    estado = models.CharField(max_length=1, choices=ESTADO, null=False, default='A')
    categoria = models.ForeignKey(SubCategoria, on_delete=models.PROTECT)
    ambiente = models.ForeignKey(Ambiente, on_delete=models.PROTECT, null=True, blank=True, related_name='mobiliarios')
    def __str__(self):
        return self.codigo