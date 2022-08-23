# Django import:
from django.db import models

# Basic models import:
from network.all.base_model.models.identification import IdentificationModel
from network.all.base_model.models.data_time import DataTimeModel
from network.all.base_model.models.status import StatusModel

# manager import:
from network.inventory.managers.device_type import DeviceTypeManager


# Credential model:
class DeviceType(DataTimeModel, StatusModel, IdentificationModel):
    """ Xxx. """

    class Meta:
        
        # Model name values:
        verbose_name = 'Device type'
        verbose_name_plural = 'Device types'

        # Default ordering:
        ordering = ['name']

    # Model objects manager:
    objects = DeviceTypeManager()

    # Main model values:
    netmiko_name = models.CharField(
        verbose_name='Netmiko name',
        help_text='Netmiko name.',
        max_length=32,
        unique=True
    )
