# Django Import:
from django.db import models

# Extended Model Import:
from inventory.all.base_model.extended_model import ExtendedModel

# Models Import:
from inventory.devices.models.credential import Credential
from inventory.devices.models.device import Device

# Change log Import:
from messages.changes.follow_change_log import follow_change_log


# Folder model:
class Group(ExtendedModel):
    """ Folders allow you to group network devices. """

    class Meta:
        
        # Model name values:
        verbose_name = 'Group'
        verbose_name_plural = 'Groups'

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
    )

    # Defaults main values:
    ssh_port = models.IntegerField(
        verbose_name='Default SSH port',
        help_text='SSH protocol port number.',
        null=True,
        blank=True,
    )
    https_port = models.IntegerField(
        verbose_name='Default HTTPS port',
        help_text='HTTPS protocol port number.',
        null=True,
        blank=True,
    )

    # Default security and credentials values:
    credential = models.ForeignKey(
        Credential,
        verbose_name='Default credential',
        help_text='Credential needed to establish SSH / HTTPS connection.',
        on_delete=models.PROTECT,
        null=True,
        blank=True,
    )
    secret = models.CharField(
        verbose_name='Default secret password',
        help_text='Network device secret password.',
        max_length=64,
        null=True,
        blank=True,
    )
    token = models.CharField(
        verbose_name='Default API token',
        help_text='Network device API key.',
        max_length=128,
        null=True,
        blank=True,
    )
    certificate = models.BooleanField(
        verbose_name='Default certificate',
        help_text='Check network device certificate during HTTPS connection.',
        null=True,
        blank=True,
    )

# Follow change log:
follow_change_log(Group)
