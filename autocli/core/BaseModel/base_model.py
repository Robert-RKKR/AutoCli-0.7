# Django Import:
from django.db import models

# Django Import:
from django.db import models

# Import django User model:
from django.contrib.auth.models import User


# Base models class:
class BaseModel(models.Model):

    class Meta:
        
        # Model name values:
        verbose_name = 'Base model'
        verbose_name_plural = 'Base models'

        # Abstract class value:
        abstract = True

    # Deleted information:
    deleted = models.BooleanField(
        verbose_name='Deleted',
        help_text=f'Is object deleted.',
        default=False,
    )

    # Model data time information:
    created = models.DateTimeField(
        verbose_name='Created',
        help_text=f'Object create date.',
        auto_now_add=True,
    )
    updated = models.DateTimeField(
        verbose_name='Updated',
        help_text=f'object last update date.',
        auto_now=True,
    )
