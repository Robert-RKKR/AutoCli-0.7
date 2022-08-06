# Django Import:
from django.db import models

# Extended Model Import:
from core.base_model.extended_model import ExtendedModel


# Credential model:
class Credential(ExtendedModel):
    """ 
    The Credential specifies the login information (Login, password)
    needed in the login process when connecting to network devices.
    """

    class Meta:
        
        # Model name values:
        verbose_name = 'Device credential'
        verbose_name_plural = 'Device credentials'

    # Main model values:
    username = models.CharField(
        verbose_name='Username',
        help_text='Local / remote user name.',
        max_length=64,
        error_messages={
            'null': 'Username field is mandatory.',
            'blank': 'Username field is mandatory.',
            'invalid': 'Enter the correct username value.',
        },
    )
    password = models.CharField(
        verbose_name='Password',
        help_text='Local / remote user password.',
        max_length=64,
    )
