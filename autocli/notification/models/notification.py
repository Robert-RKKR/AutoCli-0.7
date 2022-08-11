# Django Import:
from django.db import models

# Application model Import:
from core.models.content_type import ContentType

# Constants:
TYPE = (
    (1, 'CRITICAL'),
    (2, 'ERROR'),
    (3, 'WARNING'),
    (4, 'INFO'),
    (5, 'DEBUG'),
)


# Logger models:
class Notification(models.Model):

    class Meta:
        
        # Model name values:
        verbose_name = 'Notification'
        verbose_name_plural = 'Notifications'
    
    # Model data time information:
    timestamp = models.DateTimeField(
        verbose_name='Timestamp',
        help_text='Time of the change creation.',
        auto_now_add=True,
    )

    # Information about correlated object:
    content_type = models.ForeignKey(
        ContentType,
        verbose_name='Content type',
        help_text='Administrator responsible for change.',
        on_delete=models.PROTECT,
        null=True,
        blank=True,
    )
    object_id = models.IntegerField(
        verbose_name='Object ID',
        help_text='Correlated object ID representation.',
        null=True,
        blank=True,
    )

    # Notification type:
    type = models.IntegerField(
        verbose_name='Notification type',
        help_text='Type of notification message.',
        choices=TYPE,
    )

    # Notification data:
    message = models.CharField(
        verbose_name='Message',
        help_text='Notification message.',
        max_length=128,
    )

    # Model representation:
    def __str__(self) -> str:
        return f'{self.pk} - {self.message}'
