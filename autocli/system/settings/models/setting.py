# Django import:
from django.db import models

# Validators Import:
from ..validators.base_validators import DescriptionValueValidator
from ..validators.base_validators import NameValueValidator

# Administrator model:
class Setting(models.Model):

    class Meta:
        
        # Model name values:
        verbose_name = 'Setting'
        verbose_name_plural = 'Settings'

        # Default ordering:
        ordering = ['pk']

    # Model validators:
    name_validator = NameValueValidator()
    description_validator = DescriptionValueValidator()

    # Setting name:
    name = models.CharField(
        verbose_name='Name',
        help_text='Settings profile name.',
        max_length=64,
        unique=True,
        validators=[name_validator],
        error_messages={
            'null': 'Name field is mandatory.',
            'blank': 'Name field is mandatory.',
            'unique': 'Settings profile with this name already exists.',
            'invalid': 'Enter the correct name value. It must contain 3 to 64 digits, letters or special characters -, _ or spaces.',
        },
    )
    description = models.CharField(
        verbose_name='Description',
        help_text='Settings profile description.',
        max_length=256,
        default='Object default description.',
        validators=[description_validator],
        error_messages={
            'invalid': 'Enter the correct description value. It must contain 8 to 256 digits, letters and special characters -, _, . or spaces.',
        },
        null=True,
        blank=True,
    )

    # Current main settings:
    current = models.BooleanField(
        verbose_name='Current',
        help_text='Current main application settings.',
        default=False,
    )

    # Settings values:
    default_username = models.CharField(
        verbose_name='Default username',
        help_text='Default username used by AutoCli for SSH connections.',
        max_length=124,
        default='cisco'
    )
    default_password = models.CharField(
        verbose_name='Default password',
        help_text='Default password used by AutoCli for SSH connections.',
        max_length=124,
        default='!Cisco@123'
    )
    history_length = models.SmallIntegerField(
        verbose_name='History length',
        help_text='Number of updates stored in the database (Without snapshot).',
        default=10
    )
    max_workers = models.SmallIntegerField(
        verbose_name='Max number of workers',
        help_text='Amount of simultaneous SSH network connections.',
        default=10
    )

    # Model representation:
    def __str__(self) -> str:
        return f'{self.pk}'
