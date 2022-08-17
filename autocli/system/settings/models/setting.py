# Django import:
from django.db import models

# Administrator model:
class Setting(models.Model):

    class Meta:
        
        # Model name values:
        verbose_name = 'Setting'
        verbose_name_plural = 'Settings'

        # Default ordering:
        ordering = ['pk']

    # Settings values:
    default_username = models.CharField(
        verbose_name='Default username',
        help_text='Default username used by AutoCli for SSH connections.',
        max_length=64,
    )
    default_password = models.CharField(
        verbose_name='Default password',
        help_text='Default password used by AutoCli for SSH connections.',
        max_length=64,
        null=True,
        blank=True,
    )

    # Model representation:
    def __str__(self) -> str:
        return f'{self.pk}'
