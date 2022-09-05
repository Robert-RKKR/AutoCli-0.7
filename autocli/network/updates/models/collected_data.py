# Django import:
import imp
from django.db import models

# Basic models import:
from network.all.base_model.models.data_time import DataTimeModel
from network.all.base_model.models.status import StatusModel

# manager import:
from network.inventory.managers.credential import CredentialManager

# Other models Import:
from .update import Update


# Collected data model:
class CollectedData(DataTimeModel, StatusModel):
    """
    Xxx.
    """

    class Meta:
        
        # Model name values:
        verbose_name = 'Collected data'
        verbose_name_plural = 'Collected data'

        # Default ordering:
        ordering = ['id']

    # Model objects manager:
    objects = CredentialManager()

    
    # Corelation witch device model:
    update = models.ForeignKey(
        Update,
        verbose_name='Update model',
        help_text='Correlated update model.',
        on_delete=models.CASCADE,
    )

    # Status values:
    result_status = models.BooleanField(
        verbose_name='Result status',
        help_text='A positive result means that the command output was successfully received and processed.',
        default=False,
    )
    raw_data_status = models.BooleanField(
        verbose_name='Raw data status',
        help_text='A positive result means that the raw data collection process has been successfully completed.',
        default=False,
    )
    processed_data_status = models.BooleanField(
        verbose_name='Processed data status',
        help_text='A positive result means that the process of processing the data was completed successfully.',
        default=False,
    )

    # Main model values:
    command_name = models.CharField(
        verbose_name='Command name',
        help_text='CLI command name.',
        max_length=64,
    )
    command_raw_data = models.TextField(
        verbose_name='Command raw data',
        help_text='CLI command raw data output.',
        null=True,
        blank=True,
    )
    command_processed_data = models.JSONField(
        verbose_name='Command processed data',
        help_text='CLI command FSM process data.',
        null=True,
        blank=True,
    )
