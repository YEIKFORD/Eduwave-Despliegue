from django.db import models
from django.contrib.auth.models import AbstractUser
from .rol import Rol
from .ficha import Ficha
from .centro_formacion import CentroFormacion


class Usuario(AbstractUser):
    TIPO_DOC = [
        ('TI', 'Tarjeta de identidad'),
        ('CC', 'Cédula de ciudadanía'),
        ('CE', 'Cédula de extranjería'),
        ('PEP', 'Permiso especial de permanencia'),
        ('PPT', 'Permiso por protecction especial'),
        ('OT', 'Otro'),
    ]
    tipo_doc = models.CharField(max_length=3, choices=TIPO_DOC, default='CC')
    telefono = models.CharField(max_length=10, blank=True, null=True)
    numero_doc = models.CharField(max_length=30, unique=True, default="")
    rol = models.ForeignKey(Rol, on_delete=models.PROTECT)
    fichas = models.ManyToManyField(Ficha, blank=True)
    centro = models.ForeignKey(CentroFormacion, on_delete=models.PROTECT)
    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"
    
    def __str__(self):
        return self.username