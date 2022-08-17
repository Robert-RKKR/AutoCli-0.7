# Django Import:
import imp
from django.db import models

# Extended Model Import:
from inventory.all.base_model.extended_model import ExtendedModel

# Change log Import:
from messages.changes.follow_change_log import follow_change_log

# manager import:
from inventory.devices.managers.credential import CredentialManager


# Credential model:
class Credential(ExtendedModel):
    """ 
    The Credential specifies the login information (Login, password)
    needed in the login process when connecting to network devices.
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
        max_length=64,
    )
    password = models.CharField(
        verbose_name='Password',
        help_text='Local / remote user password.',
        max_length=64,
    )

# Follow change log:
follow_change_log(Credential)
