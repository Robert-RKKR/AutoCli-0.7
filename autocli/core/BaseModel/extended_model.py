# Django Import:
from django.db import models

# Base model Import:
from .base_model import BaseModel

# Validators Import:
from .validators import DescriptionValueValidator
from .validators import NameValueValidator


# Base models class:
class ExtendedModel(BaseModel):

    class Meta:
        
        # Model name values:
        verbose_name = 'Extended model'
        verbose_name_plural = 'Extended models'

        # Abstract class value:
        abstract = True

    # Model validators:
    name_validator = NameValueValidator()
    description_validator = DescriptionValueValidator()
    
    # Class name value:
    class_name = Meta.verbose_name

    # Model status values:
    root = models.BooleanField(
        verbose_name='Root',
        help_text=f'Root object cannot be deleted.',
        default=False
    )
    active = models.BooleanField(
        verbose_name='Active',
        help_text=f'Object status.',
        default=True
    )

    # Main model values:
    name = models.CharField(
        verbose_name='Name',
        help_text=f'Object name.',
        max_length=32,
        blank=False,
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
        help_text=f'Object description.',
        max_length=256,
        default=f'Object default description.',
        validators=[description_validator],
        error_messages={
            'invalid': 'Enter the correct description value. It must contain 8 to 256 digits, letters and special characters -, _, . or spaces.',
        },
    )

    # Model representation:
    def __repr__(self) -> str:
        return f'{self.pk}: {self.name}'

    def __str__(self) -> str:
        return  f'{self.pk}: {self.name}'
