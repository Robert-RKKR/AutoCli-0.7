# Django import:
import django_filters

# Base filter import:
from inventory.all.base_model.filters.base_filter import BaseFilter

# Model import:
from inventory.devices.models.device import Device


# Filters:
class DeviceFilter(BaseFilter):

    class Meta:

        model = Device
