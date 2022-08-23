# Django import:
from django.db import models

# Basic models import:
from network.all.base_model.models.identification import IdentificationModel
from network.all.base_model.models.data_time import DataTimeModel
from network.all.base_model.models.status import StatusModel

# Models import:
from network.inventory.models.credential import Credential
from network.inventory.models.device import Device

# manager import:
from network.inventory.managers.group import GroupManager


# Folder model:
class Group(DataTimeModel, StatusModel, IdentificationModel):
    """ Folders allow you to group network inventory. """

    class Meta:
        
        # Model name values:
        verbose_name = 'Group'
        verbose_name_plural = 'Groups'

        # Default ordering:
        ordering = ['name']

    # Model objects manager:
    objects = GroupManager()

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
        help_text='All inventory that belongs to current folder.',
        blank=True,
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
