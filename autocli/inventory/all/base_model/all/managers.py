# Django Import:
from django.db.models import Manager


# Managers class:
class BaseManager(Manager):

    def get_queryset(self):
        return super(
            BaseManager, self
        ).get_queryset().filter(deleted=False)


class ActiveManager(Manager):

    def get_queryset(self):
        return super(
            ActiveManager, self
        ).get_queryset().filter(deleted=False, active=True)
