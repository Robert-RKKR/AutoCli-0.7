# Django import:
import django_filters

# Base filter import:
from network.all.base_model.filters.base_filter import BaseFilter

# Model import:
from network.inventory.models.device import Device


# Filters:
class DeviceFilter(BaseFilter):

    class Meta:

        model = Device
