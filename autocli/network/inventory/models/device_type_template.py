# Django import:
from django.db import models

# Basic models import:
from network.all.base_model.models.data_time import DataTimeModel
from network.all.base_model.models.status import StatusModel

# Other models import:
from network.inventory.models.device_type import DeviceType

# manager import:
from network.inventory.managers.device_type_template import DeviceTypeTemplateManager

# Constants declaration:
DEVICE_DATA = (
    (0, 'None'),
    (1, 'Access list data'),
    (2, 'ARP table data'),
    (3, 'Device data'),
    (4, 'DMVPN data'),
    (5, 'Environment data'),
    (6, 'Etherchannel data'),
    (7, 'Interface data'),
    (8, 'MAC table data'),
    (9, 'Module data'),
    (10, 'Neighbor data'),
    (11, 'NHRP data'),
    (12, 'Router data'),
)


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
        related_name='device_type_templates',
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
    device_data_corelation = models.IntegerField(
        verbose_name='Update status',
        help_text='Device update status.',
        choices=DEVICE_DATA,
        default=0,
    )
    sfm_expression = models.TextField(
        verbose_name='SFM expression',
        help_text='SFM expression used to check if CLI command/s output is correct.',
    )

    # object representation:
    def __repr__(self) -> str:
        return f'{self.pk}: {self.command.capitalize()}'

    def __str__(self) -> str:
        return  f'{self.pk}: {self.command.capitalize()}'

    # Natural key representation:
    def natural_key(self):
        return str(self.command.capitalize())
