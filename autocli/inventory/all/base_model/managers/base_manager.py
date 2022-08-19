# Django Import:
from django.db.models import Manager


# Managers class:
class BaseManager(Manager):

    def get_queryset(self):
        return super(
            BaseManager, self
        ).get_queryset().filter(deleted=False)

    def get_by_natural_key(self, name):
        return self.get(name=name)
