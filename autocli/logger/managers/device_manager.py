# Django Import:
from django.db.models import Manager


# Managers class:
class LogManager(Manager):

    def get_log_extensions(self, log):
        # Application model Import:
        from logger.models.extension import Extension
        log_extension = Extension.objects.filter(
            log=log,
        )
        return log_extension

    def get_log_extensions_from_pk(self, log_pk: int):
        log = self.get(pk=log_pk)
        # Application model Import:
        from logger.models.extension import Extension
        log_extension = Extension.objects.filter(
            log=log,
        )
        return log_extension
