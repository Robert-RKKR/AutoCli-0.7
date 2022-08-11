# Django Import:
from django.db import models

# Extended Model Import:
from inventory.base_model.extended_model import ExtendedModel

# Change log Import:
from message_system.change_log.follow_change_log import follow_change_log


# Credential model:
class DeviceType(ExtendedModel):
    """ Xxx. """

    class Meta:
        
        # Model name values:
        verbose_name = 'Device type'
        verbose_name_plural = 'Device types'

    # Main model values:
    netmiko_name = models.CharField(
        verbose_name='Netmiko name',
        help_text='Netmiko name.',
        max_length=32,
        unique=True
    )

# Follow change log:
follow_change_log(DeviceType)
