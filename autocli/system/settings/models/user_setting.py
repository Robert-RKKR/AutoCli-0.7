# Django import:
from django.db import models

# Administrator model import:
from django.contrib.auth.models import User


# Administrator model:
class UserSetting(models.Model):

    class Meta:
        
        # Model name values:
        verbose_name = 'User setting'
        verbose_name_plural = 'User settings'

        # Default ordering:
        ordering = ['pk']

    # Administrator corelation:
    administrator = models.ForeignKey(
        User,
        verbose_name='Administrator',
        help_text='Settings related administrator account.',
        on_delete=models.CASCADE,
    )

    # Settings values:
    default_username = models.CharField(
        verbose_name='Default username',
        help_text='Default username used by AutoCli for SSH connections.',
        max_length=64,
        default='cisco',
    )
    default_password = models.CharField(
        verbose_name='Default password',
        help_text='Default password used by AutoCli for SSH connections.',
        max_length=64,
        default='!Cisco@123',
    )

    # Model representation:
    def __str__(self) -> str:
        return f'{self.pk} - {self.administrator}'
