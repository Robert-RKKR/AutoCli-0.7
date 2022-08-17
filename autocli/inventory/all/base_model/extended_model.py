# Django Import:
from django.core.exceptions import ValidationError
from django.db import models

# Managers Import:
from .all.managers import ActiveManager
from .all.managers import BaseManager

# Base model Import:
from .base_model import BaseModel

# Validators Import:
from .all.validators import DescriptionValueValidator
from .all.validators import NameValueValidator


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

    # Model objects manager:
    active_objects = ActiveManager()
    objects = BaseManager()

    # Model status values:
    root = models.BooleanField(
        verbose_name='Root',
        help_text='Root object cannot be deleted.',
        default=False,
    )
    active = models.BooleanField(
        verbose_name='Active',
        help_text='Object status.',
        default=True,
    )

    # Main model values:
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
    ico = models.IntegerField(
        verbose_name='Object ico',
        help_text='Object graphical representation.',
        default=1,
    )
    color = models.IntegerField(
        verbose_name='Object color',
        help_text='Color object mark.',
        default=1,
    )

    # Model Save override:
    def save(self, *args, **kwargs):
        
        # Check if object root value is true:
        if self.root is True:
            raise ValidationError('Root object cannot be changed or deleted.')

        super(ExtendedModel, self).save(*args, **kwargs)

    # Model Save override:
    def delete(self, *args, **kwargs):
        
        # Check if object root value is true:
        if self.root is True:
            raise ValidationError('Root object cannot be changed or deleted.')

        super(ExtendedModel, self).delete(*args, **kwargs)

    # Model Save override:
    def update(self, *args, **kwargs):
        
        # Check if object root value is true:
        if self.root is True:
            raise ValidationError('Root object cannot be changed or deleted.')

        super(ExtendedModel, self).update(*args, **kwargs)

    # Model representation:
    def __repr__(self) -> str:
        return f'{self.pk}: {self.name}'

    def __str__(self) -> str:
        return  f'{self.pk}: {self.name}'
