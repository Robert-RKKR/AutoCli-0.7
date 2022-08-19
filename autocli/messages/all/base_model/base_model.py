# Django Import:
from django.db import models

# Managers Import:
from .managers.base_manager import BasicManager


# Base models class:
class BaseModel(models.Model):

    class Meta:
        
        # Model name values:
        verbose_name = 'Base model'
        verbose_name_plural = 'Base models'

        # Abstract class value:
        abstract = True

    # Model objects manager:
    objects = BasicManager()
    
    # Model data time information:
    timestamp = models.DateTimeField(
        verbose_name='Timestamp',
        help_text='Time of the change creation.',
        auto_now_add=True,
    )

    # Information about correlated object:
    app_name = models.CharField(
        verbose_name='Object application name',
        help_text='Name of the object application.',
        max_length=64,
    )
    model_name = models.CharField(
        verbose_name='Object model name',
        help_text='Name of the object model.',
        max_length=64,
    )
    object_id = models.IntegerField(
        verbose_name='Object ID',
        help_text='Correlated object ID representation.',
        null=True,
        blank=True,
    )
