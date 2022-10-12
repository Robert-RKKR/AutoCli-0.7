from django.apps import AppConfig
from django.db.models.signals import post_save


class UpdatesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'network.updates'

    def ready(self):
        import network.updates.signals
