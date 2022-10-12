# Django import:
from django.db import models

# Basic models import:
from network.all.base_model.models.data_time import DataTimeModel
from network.all.base_model.models.status import StatusModel

# Manager import:
from network.inventory.managers.credential import CredentialManager

# Other models Import:
from network.updates.models.update import Update


# DMVPN data model:
class DmvpnData(DataTimeModel, StatusModel):
    """
    DMVPN data retrieved directly from the network device.
    """

    class Meta:
        
        # Model name values:
        verbose_name = 'DMVPN data'
        verbose_name_plural = 'DMVPN data'

        # Default ordering:
        ordering = ['-id']

    # Model objects manager:
    objects = CredentialManager()
    
    # Corelation witch device model:
    update = models.ForeignKey(
        Update,
        verbose_name='Update model',
        help_text='Correlated update model.',
        on_delete=models.CASCADE,
    )
