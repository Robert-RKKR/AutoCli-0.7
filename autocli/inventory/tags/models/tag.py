# Django import:
from asyncio import constants
from django.db import models

# Basic models import:
from inventory.all.base_model.models.data_time import DataTimeModel
from inventory.all.base_model.models.status import StatusModel

# Validators Import:
from inventory.all.base_model.validators.base_validators import DescriptionValueValidator
from inventory.all.base_model.validators.base_validators import NameValueValidator

# Manager import:
from inventory.tags.managers.tag import TagManager

# Color constants import:
from inventory.tags.constants.colors import COLORS, COLOR_BLUE


# Device type template model:
class Tag(DataTimeModel, StatusModel):

    class Meta:
        
        # Model name values:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'

        # Default ordering:
        ordering = ['pk']

    # Model objects manager:
    objects = TagManager()

    # Model validators:
    name_validator = NameValueValidator()
    description_validator = DescriptionValueValidator()

    # Identification values:
    name = models.CharField(
        verbose_name='Name',
        help_text='Object name.',
        max_length=32,
        unique=True,
        validators=[name_validator],
        error_messages={
            'null': 'Name field is mandatory.',
            'blank': 'Name field is mandatory.',
            'unique': 'Object with this name already exists.',
            'invalid': 'Enter the correct name value. It must contain 3 to 32 digits, letters or special characters -, _ or spaces.',
        },
    )
    description = models.CharField(
        verbose_name='Description',
        help_text='Object description.',
        max_length=256,
        default='Object default description.',
        validators=[description_validator],
        error_messages={
            'invalid': 'Enter the correct description value. It must contain 8 to 256 digits, letters and special characters -, _, . or spaces.',
        },
        null=True,
        blank=True,
    )

    # Related color:
    color = models.CharField(
        verbose_name='Color',
        help_text='Tag related color.',
        max_length=6,
        default=COLOR_BLUE,
        choices=COLORS,
    )

    # object representation:
    def __repr__(self) -> str:
        return f'{self.pk}: {self.name}'

    def __str__(self) -> str:
        return  f'{self.pk}: {self.name}'

    # Natural key representation:
    def natural_key(self):
        return str(self.name)
