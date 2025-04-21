from django.db import models

class TipoNovedad(models.Model):
    nombre = models.CharField(max_length=20, unique=True, null=False)