# Django import:
from django.db import models

# Basic models import:
from network.all.base_model.models.data_time import DataTimeModel
from network.all.base_model.models.status import StatusModel

# Manager import:
from network.inventory.managers.credential import CredentialManager

# Other models Import:
from network.updates.models.update import Update


# MAC Table data model:
class MacTableData(DataTimeModel, StatusModel):
    """
    MAC Table data retrieved directly from the network device.
    """

    class Meta:
        
        # Model name values:
        verbose_name = 'MAC Table data'
        verbose_name_plural = 'MAC Table data'

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

    # MAC table information:
    vlan = models.CharField(max_length=32, null=True, blank=True)
    mac = models.CharField(max_length=32, null=True, blank=True)
    type = models.CharField(max_length=32, null=True, blank=True)
    age = models.CharField(max_length=32, null=True, blank=True)
    secure = models.CharField(max_length=32, null=True, blank=True)
    ntfy = models.CharField(max_length=32, null=True, blank=True)
    ports = models.CharField(max_length=32, null=True, blank=True)
    ports_list = models.JSONField(null=True, blank=True)

    """Value MAC ([0-9a-fA-F]{4}\.[0-9a-fA-F]{4}\.[0-9a-fA-F]{4})
    Value TYPE (\S+)
    Value VLAN (\S+)
    Value List PORTS_LIST ([^,\s]+)"""
