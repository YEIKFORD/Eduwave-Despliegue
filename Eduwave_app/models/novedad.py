from django.db import models
from django.conf import settings
from .tipo_novedad import TipoNovedad
from .usuario import Usuario
from .ambiente import Ambiente
from .inventario import Inventario


class Novedad(models.Model):
    ESTADO = [
        ('P', 'Pendiente'),
        ('A', 'Aprobado'),
        ('C', 'Cerrado'),
    ]
    TIPO_DE_FALTA = [
        ('Leve', 'Leve'),
        ('Grave', 'Grave'),
        ('Gravisima', 'Gravísima'),
    ]
    descripcion = models.CharField(max_length=450)
    fecha = models.DateTimeField(auto_now_add=True)
    evidencia = models.FileField(upload_to='evidencias/', blank=True, null=True)
    estado = models.CharField(max_length=1, choices=ESTADO, default='P')

    tipo_novedad = models.ForeignKey(TipoNovedad, on_delete=models.PROTECT)

    # Campos solo para académica y disciplinaria
    tipo_falta = models.CharField(max_length=10, choices=TIPO_DE_FALTA, blank=True, null=True)
    usuarios = models.ManyToManyField(Usuario, blank=True, related_name='novedades_aprendiz')

    # Campos solo para novedad ambiental
    ambiente = models.ForeignKey(Ambiente, on_delete=models.SET_NULL, null=True, blank=True)
    inventario = models.ManyToManyField(Inventario, blank=True)

    # Usuario que creó la novedad (instructor)
    creado_por = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name='novedades_creadas')

    def _str_(self):
        return f"Novedad {self.id} - {self.tipo_novedad.nombre} - {self.descripcion[:30]}"