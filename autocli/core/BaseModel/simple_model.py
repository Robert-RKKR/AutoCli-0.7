# Django Import:
from django.db import models

# Base model Import:
from .base_model import BaseModel


# Base models class:
class SimpleModel(BaseModel):

    class Meta:
        
        # Model name values:
        verbose_name = 'Simple model'
        verbose_name_plural = 'Simple models'

        # Abstract class value:
        abstract = True

    # Model representation:
    def __repr__(self) -> str:
        return f'{self.pk}: {self.updated}'

    def __str__(self) -> str:
        return  f'{self.pk}: {self.updated}'

