# Django import:
from django.db import models

# Basic models import:
from network.all.base_model.models.data_time import DataTimeModel
from network.all.base_model.models.status import StatusModel

# manager import:
from network.inventory.managers.credential import CredentialManager

# Models Import:
from network.inventory.models.device import Device
from .snapshot import Snapshot

# Constants declaration:
STATUS = (
    (0, 'Initiation'),
    (1, 'Successfully collected data'),
    (2, 'Data collection failed')
)


# Update model:
class Update(DataTimeModel, StatusModel):
    """
    Xxx.
    """

    class Meta:
        
        # Model name values:
        verbose_name = 'Update'
        verbose_name_plural = 'Update'

        # Default ordering:
        ordering = ['-id']

    # Model objects manager:
    objects = CredentialManager()

    # Corelation with other models:
    device = models.ForeignKey(
        Device,
        verbose_name='Device',
        help_text='The network device affected by the update.',
        on_delete=models.CASCADE,
    )
    snapshot = models.ForeignKey(
        Snapshot,
        verbose_name='Snapshot',
        help_text='Correlated snapshot.',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )

    # Status values:
    status = models.IntegerField(
        verbose_name='Update status',
        help_text='Device update status.',
        choices=STATUS,
        default=0,
    )
    result_status = models.BooleanField(
        verbose_name='Result status',
        help_text='A positive result means that all commands updates was collected.',
        default=False,
    )
