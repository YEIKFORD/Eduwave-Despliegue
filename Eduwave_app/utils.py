from django.core.mail import send_mail
from django.conf import settings
from django.urls import reverse

def enviar_correo_novedad(novedad):
    asunto = f"Nueva novedad registrada: {novedad.tipo_novedad.nombre}"
    
    # Correos: el creador + usuarios involucrados
    destinatarios = [novedad.creado_por.email] + [
        u.email for u in novedad.usuarios.all() if u.email
    ]
    # Quitar duplicados
    destinatarios = list(set(destinatarios))


    mensaje = f"""
    Se ha registrado una nueva novedad en el sistema Eduwave.

    Resumen:
    - Tipo de novedad: {novedad.tipo_novedad.nombre}
    - Fecha de creación: {novedad.fecha.strftime('%d/%m/%Y')}
    - Estado actual: {'Pendiente' if novedad.estado == 'P' else novedad.get_estado_display()}
    - Registrada por: {novedad.creado_por.get_full_name() or novedad.creado_por.username}

    Te invitamos a ingresar al sistema para consultar los detalles completos y, si es tu responsabilidad, realizar el seguimiento correspondiente.

    Este es un mensaje automático. Por favor, no respondas a este correo.
    """

    send_mail(
        asunto,
        mensaje,
        settings.EMAIL_HOST_USER,
        destinatarios,
        fail_silently=False
    )