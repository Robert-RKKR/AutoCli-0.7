# Django Import:
from django.core.exceptions import ValidationError
from django.db import models


# Base models class:
class StatusModel(models.Model):

    class Meta:
        
        # Abstract class value:
        abstract = True

    # Deleted information:
    deleted = models.BooleanField(
        verbose_name='Deleted',
        help_text='Is object deleted.',
        default=False,
    )

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

    # Model Save override:
    def save(self, *args, **kwargs):
        
        # Check if object root value is true:
        if self.root is True:
            pass
            # raise ValidationError('Root object cannot be changed or deleted.')
        else:
            super(StatusModel, self).save(*args, **kwargs)

    # Model Save override:
    def delete(self, *args, **kwargs):
        
        # Check if object root value is true:
        if self.root is True:
            pass
            # raise ValidationError('Root object cannot be changed or deleted.')
        else:
            super(StatusModel, self).delete(*args, **kwargs)

    # Model Save override:
    def update(self, *args, **kwargs):
        
        # Check if object root value is true:
        if self.root is True:
            pass
            # raise ValidationError('Root object cannot be changed or deleted.')
        else:
            super(StatusModel, self).update(*args, **kwargs)

    # object representation:
    def __repr__(self) -> str:
        return str(self.pk)

    def __str__(self) -> str:
        return  str(self.pk)

    # Natural key representation:
    def natural_key(self):
        return str(self.pk)
