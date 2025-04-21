from django.apps import AppConfig

class EduwaveAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Eduwave_app'
    def ready(self):
        import Eduwave_app.signals

