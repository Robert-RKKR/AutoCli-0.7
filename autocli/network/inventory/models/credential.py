# Django import:
from django.db import models

# Basic models import:
from network.all.base_model.models.identification import IdentificationModel
from network.all.base_model.models.data_time import DataTimeModel
from network.all.base_model.models.status import StatusModel

# manager import:
from network.inventory.managers.credential import CredentialManager


# Credential model:
class Credential(DataTimeModel, StatusModel, IdentificationModel):
    """ 
    The Credential specifies the login information (Login, password)
    needed in the login process when connecting to network inventory.
    """

    class Meta:
        
        # Model name values:
        verbose_name = 'Credential'
        verbose_name_plural = 'Credentials'

        # Default ordering:
        ordering = ['name']

    # Model objects manager:
    objects = CredentialManager()

    # Main model values:
    username = models.CharField(
        verbose_name='Username',
        help_text='Local / remote user name.',
        max_length=124,
    )
    password = models.CharField(
        verbose_name='Password',
        help_text='Local / remote user password.',
        max_length=124,
    )
