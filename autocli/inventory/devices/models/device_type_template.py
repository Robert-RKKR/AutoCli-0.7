# Django import:
from django.db import models

# Basic models import:
from inventory.all.base_model.models.data_time import DataTimeModel
from inventory.all.base_model.models.status import StatusModel

# Other models import:
from inventory.devices.models.device_type import DeviceType

# manager import:
from inventory.devices.managers.device_type_template import DeviceTypeTemplateManager


# Device type template model:
class DeviceTypeTemplate(DataTimeModel, StatusModel):
    """
    CLI command template can be processed to receive CLI configurations commands.
    A TextFSM string or Regex expression can then be used to check that the received output is correct.
    """

    class Meta:
        
        # Model name values:
        verbose_name = 'Device type template'
        verbose_name_plural = 'Device type templates'

        # Default ordering:
        ordering = ['pk']

        # Unique values:
        unique_together = [['command', 'device_type']]

    # Model objects manager:
    objects = DeviceTypeTemplateManager()

    # Spacial type of Device type template object:
    special = models.BooleanField(
        verbose_name='Special template',
        help_text='Spacial type of Device type template object.',
        default=False,
    )
    vrf = models.BooleanField(
        verbose_name='VRF template',
        help_text='VRF cli command template.',
        default=False,
    )

    # Device type corelation:
    device_type = models.ForeignKey(
        DeviceType,
        verbose_name='Device type',
        help_text='Type of network device system.',
        on_delete=models.PROTECT,
    )

    # SSH commands values:
    command = models.CharField(
        verbose_name='CLI command',
        help_text='CLI command that will be executed on network device.',
        max_length=64,
    )
    sfm_expression = models.TextField(
        verbose_name='SFM expression',
        help_text='SFM expression used to check if CLI command/s output is correct.',
    )

    # Model representation:
    def __repr__(self) -> str:
        return f'{self.pk}: {self.device_type}/{self.command.capitalize()}'

    def __str__(self) -> str:
        return  f'{self.pk}: {self.device_type}/{self.command.capitalize()}'

    # Natural key representation:
    def natural_key(self):
        return f'{self.device_type}/{self.command.capitalize()}'
