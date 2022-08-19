# Django Import:
from django.db import models

# Managers Import:
from .managers.base_manager import BaseManager


# Base models class:
class BaseModel(models.Model):

    class Meta:
        
        # Model name values:
        verbose_name = 'Base model'
        verbose_name_plural = 'Base models'

        # Abstract class value:
        abstract = True

    # Model objects manager:
    objects = BaseManager()

    # Deleted information:
    deleted = models.BooleanField(
        verbose_name='Deleted',
        help_text='Is object deleted.',
        default=False,
    )

    # Model data time information:
    created = models.DateTimeField(
        verbose_name='Created',
        help_text='Object create date.',
        auto_now_add=True,
    )
    updated = models.DateTimeField(
        verbose_name='Updated',
        help_text='object last update date.',
        auto_now=True,
    )
