# Django import:
import imp
from django.db import models

# Basic models import:
from network.all.base_model.models.identification import IdentificationModel
from network.all.base_model.models.data_time import DataTimeModel
from network.all.base_model.models.status import StatusModel

# manager import:
from network.inventory.managers.credential import CredentialManager


# Snapshot model:
class Snapshot(DataTimeModel, StatusModel, IdentificationModel):
    """
    Xxx.
    """

    class Meta:
        
        # Model name values:
        verbose_name = 'Snapshot'
        verbose_name_plural = 'Snapshots'

        # Default ordering:
        ordering = ['name']

    # Model objects manager:
    objects = CredentialManager()
