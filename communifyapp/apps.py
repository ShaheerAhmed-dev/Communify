from django.apps import AppConfig


class CommunifyappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'communifyapp'

    def ready(self):
        from . import signals
