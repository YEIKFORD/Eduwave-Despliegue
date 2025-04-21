from django.core.mail import send_mail
from django.conf import settings

def enviar_correo_novedad(novedad):
    # Obtener los correos electrónicos de los involucrados
    correos = [novedad.creado_por.email]  # El usuario que crea la novedad
    for usuario in novedad.usuarios.all():  # Los usuarios involucrados
        correos.append(usuario.email)

    # Enviar correo
    asunto = 'Nueva Novedad Creada'
    mensaje = f'Una nueva novedad ha sido registrada: {novedad.descripcion}'
    send_mail(asunto, mensaje, settings.EMAIL_HOST_USER, correos)
