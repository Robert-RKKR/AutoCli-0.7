# Django Import:
from django.db import models

# Extended Model Import:
from inventory.base_model.simple_model import SimpleModel

# Other models Import:
from inventory.models.device_type import DeviceType

# Change log Import:
from message_system.change_log.follow_change_log import follow_change_log


# Device type template model:
class DeviceTypeTemplate(SimpleModel):
    """
    CLI command template can be processed to receive CLI configurations commands.
    A TextFSM string or Regex expression can then be used to check that the received output is correct.
    """

    class Meta:
        
        # Model name values:
        verbose_name = 'Device type template'
        verbose_name_plural = 'Device type templates'

        # Unique values:
        unique_together = [['command', 'device_type']]

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
        null=True,
        blank=True
    )
    sfm_expression = models.TextField(
        verbose_name='SFM expression',
        help_text='SFM expression used to check if CLI command/s output is correct.',
        null=True,
        blank=True
    )

    # Model representation:
    def __repr__(self) -> str:
        return f'{self.pk}: {self.command.capitalize()}'

    def __str__(self) -> str:
        return  f'{self.pk}: {self.command.capitalize()}'

# Follow change log:
follow_change_log(DeviceTypeTemplate)
