from django.apps import AppConfig


class ChangeLogConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'change_log'

    def ready(self):
        import change_log.signals
