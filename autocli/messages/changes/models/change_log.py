# Django import:
from django.db import models

# Administrator model import:
from django.contrib.auth.models import User

# Manager Import:
from messages.changes.managers import ChangeLogManager

# Base model import:
from messages.all.base_model.base_model import BaseModel

# Constants declaration:
ACTION = (
    (0, '---'),
    (1, 'Create'),
    (2, 'Update'),
    (3, 'Delete')
)


# Device model:
class ChangeLog(BaseModel):
    """ Xxx. """

    class Meta:
        # Model name values:
        verbose_name = 'Change log'
        verbose_name_plural = 'Change logs'

        # Default ordering:
        ordering = ['-pk']

    # Model objects manager:
    objects = ChangeLogManager()

    # Correlation witch user model:
    administrator = models.ForeignKey(
        User,
        verbose_name='Administrator',
        help_text='Administrator responsible for change.',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    # Action:
    action = models.IntegerField(
        verbose_name='Change log action',
        help_text='The action that was performed on a given model.',
        choices=ACTION,
        default=0,
    )

    # Change details:
    after = models.JSONField(
        verbose_name='JSON object representation',
        help_text='JSON object representation after changes was made, and saved to database.',
        null=True,
        blank=True,
    )

    # Model representation:
    def __repr__(self) -> str:
        return f'{self.pk}: {self.action}'

    def __str__(self) -> str:
        return f'{self.pk}: {self.action}'

