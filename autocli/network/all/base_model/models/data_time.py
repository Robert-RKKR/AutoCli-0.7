# Django Import:
from django.db import models


# Base models class:
class DataTimeModel(models.Model):

    class Meta:

        # Abstract class value:
        abstract = True

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
