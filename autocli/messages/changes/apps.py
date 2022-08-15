from django.apps import AppConfig

from django.db.models.signals import post_save

class ChangesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'messages.changes'

    def ready(self):
        from .signals import base_post_signal
        post_save.connect(base_post_signal)
