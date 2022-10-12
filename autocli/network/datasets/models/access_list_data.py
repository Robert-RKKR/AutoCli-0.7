# Django import:
from django.db import models

# Basic models import:
from network.all.base_model.models.data_time import DataTimeModel
from network.all.base_model.models.status import StatusModel

# Manager import:
from network.inventory.managers.credential import CredentialManager

# Other models Import:
from network.updates.models.update import Update


# Access list data model:
class AccessListData(DataTimeModel, StatusModel):
    """
    Access list data retrieved directly from the network device.
    """

    class Meta:
        
        # Model name values:
        verbose_name = 'Access list data'
        verbose_name_plural = 'Access list data'

        # Default ordering:
        ordering = ['-id']

        # Unique together:
        unique_together = ['update', 'name', 'sn']

    # Model objects manager:
    objects = CredentialManager()
    
    # Corelation witch device model:
    update = models.ForeignKey(
        Update,
        verbose_name='Update model',
        help_text='Correlated update model.',
        on_delete=models.CASCADE,
    )

    # Access list information:
    name = models.CharField(max_length=32, null=True, blank=True)
    sn = models.IntegerField(null=True, blank=True)
    type = models.CharField(max_length=32, null=True, blank=True)
    interface = models.CharField(max_length=32, null=True, blank=True)
    interface_direction = models.CharField(max_length=32, null=True, blank=True)
