# Django Import:
from django.db import models

# Base model import:
from messages.all.base_model.base_model import BaseModel

# Manager Import:
from messages.notifications.managers.notification import NotificationManager

# Constants:
TYPE = (
    (0, 'Unknown'),
    (1, 'Critical'),
    (2, 'Error'),
    (3, 'Warning'),
    (4, 'Info'),
    (5, 'Debug'),
)


# Notification models:
class Notification(BaseModel):

    class Meta:
        
        # Model name values:
        verbose_name = 'Notification'
        verbose_name_plural = 'Notifications'

        # Default ordering:
        ordering = ['-pk']

    # Model objects manager:
    objects = NotificationManager()

    # Notification type:
    type = models.IntegerField(
        verbose_name='Notification type',
        help_text='Type of notification message.',
        choices=TYPE,
        default=4,
    )

    # Notification main data:
    application = models.CharField(
        verbose_name='Application',
        help_text='Name of the application which triggered the notification.',
        max_length=64,
    )
    message = models.CharField(
        verbose_name='Message',
        help_text='Notification message.',
        max_length=128,
    )

    # Model representation:
    def __str__(self) -> str:
        return f'{self.pk} - {self.message}'
