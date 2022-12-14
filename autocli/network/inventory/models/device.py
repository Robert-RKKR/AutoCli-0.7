# Django import:
from django.db import models

# Basic models import:
from network.all.base_model.models.identification import IdentificationModel
from network.all.base_model.models.data_time import DataTimeModel
from network.all.base_model.models.status import StatusModel

# Application models import:
from network.inventory.models.device_type import DeviceType
from network.inventory.models.credential import Credential

# Manager import:
from network.inventory.managers.device import DeviceManager

# Validators import:
from network.inventory.validators import HostnameValueValidator


# Device model:
class Device(DataTimeModel, StatusModel, IdentificationModel):
    """ 
    Devices is the main component of the AutoCli application,
    it contains basic network Information about inventory that
    are not collected directly from the inventory themselves.
    """

    class Meta:
        
        # Model name values:
        verbose_name = 'Device'
        verbose_name_plural = 'Devices'

        # Default ordering:
        ordering = ['-pk']

    # Validators:
    hostname_validator = HostnameValueValidator()

    # Model objects manager:
    objects = DeviceManager()

    # Main model values:
    hostname = models.CharField(
        verbose_name='Hostname',
        help_text='Valid IP address or domain name.',
        max_length=32,
        unique=True,
        validators=[hostname_validator],
        error_messages={
            'null': 'IP / DNS name field is mandatory.',
            'blank': 'IP / DNS name field is mandatory.',
            'unique': 'Device with this hostname already exists.',
            'invalid': 'Enter a valid IP address or DNS resolvable hostname. It must contain 4 to 32 digits, letters and special characters -, _, . or spaces.',
        },
    )
    ssh_port = models.IntegerField(
        verbose_name='SSH port',
        help_text='SSH protocol port number.',
        null=True,
        blank=True,
    )
    https_port = models.IntegerField(
        verbose_name='HTTPS port',
        help_text='HTTPS protocol port number.',
        null=True,
        blank=True,
    )

    # Corelation witch device type model:
    device_type = models.ForeignKey(
        DeviceType,
        related_name='devices',
        verbose_name='Device type',
        help_text='Type of network device system.',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )

    # Device status:
    ssh_status = models.BooleanField(
        verbose_name='SSH status',
        help_text='Status of SSH connection to the device.',
        default=False,
    )
    https_status = models.BooleanField(
        verbose_name='HTTPS status',
        help_text='Status of HTTPS connection to the device.',
        default=False,
    )

    # Security and credentials:
    credential = models.ForeignKey(
        Credential,
        related_name='devices',
        verbose_name='Credential',
        help_text='Credential needed to establish SSH / HTTPS connection.',
        on_delete=models.PROTECT,
        null=True,
        blank=True,
    )
    secret = models.CharField(
        verbose_name='Secret password',
        help_text='Network device secret password.',
        max_length=64,
        null=True,
        blank=True,
    )
    token = models.CharField(
        verbose_name='API token',
        help_text='Network device API key.',
        max_length=128,
        null=True,
        blank=True,
    )
    certificate = models.BooleanField(
        verbose_name='Certificate',
        help_text='Check network device certificate during HTTPS connection.',
        default=False,
    )
