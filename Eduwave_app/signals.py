# signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Novedad
from .utils import enviar_correo_novedad

@receiver(post_save, sender=Novedad)
def enviar_correo_al_crear_novedad(sender, instance, created, **kwargs):
    if created:
        print(f"Novedad creada: {instance.descripcion}")
        enviar_correo_novedad(instance)
