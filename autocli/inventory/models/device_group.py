# Django Import:
from django.db import models

# Extended Model Import:
from core.base_model.extended_model import ExtendedModel

# Models Import:
from inventory.models.device_credential import DeviceCredential
from inventory.models.device import Device


# Folder model:
class DeviceGroup(ExtendedModel):
    """ Folders allow you to group network devices. """

    class Meta:
        
        # Model name values:
        verbose_name = 'Device group'
        verbose_name_plural = 'Device groups'

    # Corelation witch other folder model:
    root_folder = models.ForeignKey(
        'self',
        verbose_name='Root folder',
        help_text='The parent folder to witch the current folder belongs.',
        on_delete=models.PROTECT,
        null=True,
        blank=True,
    )

    # Corelation witch device model:
    devices = models.ManyToManyField(
        Device,
        verbose_name='Devices',
        help_text='All devices that belongs to current folder.',
        null=True,
        blank=True,
    )

    # Defaults main values:
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

    # Default security and credentials values:
    credential = models.ForeignKey(
        DeviceCredential,
        verbose_name='Credential',
        help_text='Credential needed to establish SSH / HTTPS connection.',
        on_delete=models.PROTECT,
        null=True,
        blank=True,
    )
    secret = models.CharField(
        verbose_name='Secret',
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
        null=True,
        blank=True,
    )
