# Django import:
from django.db import models

# Basic models import:
from network.all.base_model.models.data_time import DataTimeModel
from network.all.base_model.models.status import StatusModel

# Manager import:
from network.inventory.managers.credential import CredentialManager

# Other models Import:
from network.updates.models.update import Update


# Module data model:
class ModuleData(DataTimeModel, StatusModel):
    """
    Module data retrieved directly from the network device.
    """

    class Meta:
        
        # Model name values:
        verbose_name = 'Module data'
        verbose_name_plural = 'Module data'

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
