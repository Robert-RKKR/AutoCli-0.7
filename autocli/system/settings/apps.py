from django.apps import AppConfig
from django.db.models.signals import post_save


class SettingsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'system.settings'

    def ready(self):
        import system.settings.signals
