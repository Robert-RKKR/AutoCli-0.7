# Django Import:
from django.db import models

# Django user model Import:
from django.contrib.auth.models import User

# Application model Import:
from change_log.models.content_type import ContentType

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

    # Model data time information:
    changed = models.DateTimeField(
        verbose_name='Changed',
        help_text='Change create date.',
        auto_now_add=True
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

    # Change object details:
    content_type = models.ForeignKey(
        ContentType,
        verbose_name='Content type',
        help_text='Administrator responsible for change.',
        on_delete=models.PROTECT,
    )
    object_id = models.IntegerField(
        verbose_name='Object ID',
        help_text='Object ID representation.'
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
        return f'{self.pk}: {self.changed}'

    def __str__(self) -> str:
        return f'{self.pk}: {self.changed}'

