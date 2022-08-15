# Django Import:
from django.db import models

# Django user model Import:
from django.contrib.auth.models import User

# Constants declaration:
ACTION = (
    (0, '---'),
    (1, 'Create'),
    (2, 'Update'),
    (3, 'Delete')
)


# Device model:
class ChangeLog(models.Model):
    """ Xxx. """

    class Meta:
        # Model name values:
        verbose_name = 'Change log'
        verbose_name_plural = 'Change logs'

        # Default ordering:
        ordering = ['-pk']

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
    )

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

