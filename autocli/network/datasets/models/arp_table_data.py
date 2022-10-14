# Django import:
from ctypes import addressof
from typing import Protocol
from django.db import models
from paramiko import agent

# Basic models import:
from network.all.base_model.models.data_time import DataTimeModel
from network.all.base_model.models.status import StatusModel

# Manager import:
from network.inventory.managers.credential import CredentialManager

# Other models Import:
from network.updates.models.update import Update


# ARP table data model:
class ArpTableData(DataTimeModel, StatusModel):
    """
    ARP table data retrieved directly from the network device.
    """

    class Meta:
        
        # Model name values:
        verbose_name = 'ARP table data'
        verbose_name_plural = 'ARP table data'

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

    # ARP table information:
    protocol = models.CharField(max_length=32, null=True, blank=True)
    address = models.CharField(max_length=32, null=True, blank=True)
    age = models.CharField(max_length=32, null=True, blank=True)
    mac = models.CharField(max_length=32, null=True, blank=True)
    type = models.CharField(max_length=32, null=True, blank=True)
    interface = models.CharField(max_length=32, null=True, blank=True)
    physical_interface = models.CharField(max_length=32, null=True, blank=True)
    cpu = models.CharField(max_length=32, null=True, blank=True)
