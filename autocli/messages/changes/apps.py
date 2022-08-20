from django.apps import AppConfig
from django.db.models.signals import post_save, post_delete

class ChangesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'messages.changes'

    def ready(self):
        from .signals import post_save_change_signal, post_delete_change_signal
        post_save.connect(post_save_change_signal)
        post_delete.connect(post_delete_change_signal)
