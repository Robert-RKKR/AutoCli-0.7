# Django import:
from django.db import models

# Basic models import:
from network.all.base_model.models.data_time import DataTimeModel
from network.all.base_model.models.status import StatusModel

# manager import:
from network.inventory.managers.credential import CredentialManager


# Device data model:
class DeviceData(DataTimeModel, StatusModel):
    """
    Main device data.
    """

    class Meta:
        
        # Model name values:
        verbose_name = 'Collected data'
        verbose_name_plural = 'Collected data'

        # Default ordering:
        ordering = ['-id']

    # Model objects manager:
    objects = CredentialManager()

    # VERSION - ALL:
    VERSION = models.CharField(max_length=32, null=True, blank=True)
    UPTIME = models.CharField(max_length=64, null=True, blank=True)
    HOSTNAME = models.CharField(max_length=128, null=True, blank=True)
    HARDWARE = models.CharField(max_length=128, null=True, blank=True)
    HARDWARE_LIST = models.JSONField(null=True, blank=True)
    IMAGE = models.CharField(max_length=128, null=True, blank=True)
    RELOAD_REASON = models.CharField(max_length=128, null=True, blank=True)
    SERIAL = models.CharField(max_length=32, null=True, blank=True)
    SERIAL_LIST = models.JSONField(null=True, blank=True)

    # VERSION - ASA:
    LICENSE_MODE = models.CharField(max_length=32, null=True, blank=True)
    LICENSE_STATE = models.CharField(max_length=32, null=True, blank=True)
    MAX_INTF = models.CharField(max_length=32, null=True, blank=True)
    MAX_VLANS = models.CharField(max_length=32, null=True, blank=True)
    FAILOVER = models.CharField(max_length=32, null=True, blank=True)
    CLUSTER = models.CharField(max_length=32, null=True, blank=True)

    # VERSION - IOS:
    UPTIME_YEARS = models.CharField(max_length=32, null=True, blank=True)
    UPTIME_WEEKS = models.CharField(max_length=32, null=True, blank=True)
    UPTIME_DAYS = models.CharField(max_length=32, null=True, blank=True)
    UPTIME_HOURS = models.CharField(max_length=32, null=True, blank=True)
    UPTIME_MINUTES = models.CharField(max_length=32, null=True, blank=True)
    CONFIG_REGISTER = models.CharField(max_length=128, null=True, blank=True)
    MAC_LIST = models.JSONField(null=True, blank=True)
