# Django Import:
from django.db import models

# Extended Model Import:
from core.base_model.extended_model import ExtendedModel

# Other models Import:
from inventory.models.device_type import DeviceType


# Device type template model:
class DeviceTypeTemplate(ExtendedModel):
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
        max_length=32,
        null=True,
        blank=True
    )
    sfm_expression = models.TextField(
        verbose_name='SFM expression',
        help_text='SFM expression used to check if CLI command/s output is correct.',
        null=True,
        blank=True
    )
