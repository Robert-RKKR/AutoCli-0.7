# Django import:
from django.db import models

# Basic models import:
from network.all.base_model.models.data_time import DataTimeModel
from network.all.base_model.models.status import StatusModel

# Manager import:
from network.inventory.managers.credential import CredentialManager

# Other models Import:
from network.updates.models.update import Update


# Device data model:
class DeviceData(DataTimeModel, StatusModel):
    """
    Basic device data retrieved directly from the network device.
    """

    class Meta:
        
        # Model name values:
        verbose_name = 'Collected data'
        verbose_name_plural = 'Collected data'

        # Default ordering:
        ordering = ['-id']

    # Model objects manager:
    objects = CredentialManager()
    
    # Corelation witch device model:
    update = models.ForeignKey(
        Update,
        unique=True,
        verbose_name='Update model',
        help_text='Correlated update model.',
        on_delete=models.CASCADE,
    )

    # Show version - all:
    version = models.CharField(max_length=32, null=True, blank=True)
    uptime = models.CharField(max_length=64, null=True, blank=True)
    hostname = models.CharField(max_length=128, null=True, blank=True)
    hardware = models.CharField(max_length=128, null=True, blank=True)
    hardware_list = models.JSONField(null=True, blank=True)
    image = models.CharField(max_length=128, null=True, blank=True)
    reload_reason = models.CharField(max_length=128, null=True, blank=True)
    serial = models.CharField(max_length=32, null=True, blank=True)
    serial_list = models.JSONField(null=True, blank=True)

    # Show version - asa:
    license_mode = models.CharField(max_length=32, null=True, blank=True)
    license_state = models.CharField(max_length=32, null=True, blank=True)
    max_intf = models.CharField(max_length=32, null=True, blank=True)
    max_vlans = models.CharField(max_length=32, null=True, blank=True)
    failover = models.CharField(max_length=32, null=True, blank=True)
    cluster = models.CharField(max_length=32, null=True, blank=True)

    # Show version - ios:
    uptime_years = models.CharField(max_length=32, null=True, blank=True)
    uptime_weeks = models.CharField(max_length=32, null=True, blank=True)
    uptime_days = models.CharField(max_length=32, null=True, blank=True)
    uptime_hours = models.CharField(max_length=32, null=True, blank=True)
    uptime_minutes = models.CharField(max_length=32, null=True, blank=True)
    config_register = models.CharField(max_length=128, null=True, blank=True)
    mac_list = models.JSONField(null=True, blank=True)

    # Show clock - all:
    time = models.CharField(max_length=32, null=True, blank=True)
    timezone = models.CharField(max_length=32, null=True, blank=True)
    dayweek = models.CharField(max_length=16, null=True, blank=True)
    month = models.CharField(max_length=16, null=True, blank=True)
    day = models.CharField(max_length=16, null=True, blank=True)
    year = models.CharField(max_length=16, null=True, blank=True)
