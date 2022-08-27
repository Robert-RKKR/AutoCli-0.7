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
        fields = {
            'name': ['exact'],
            'description': ['exact'],
            'hostname': ['exact'],
            'ssh_port': ['exact'],
            'https_port': ['exact'],
            'device_type': ['exact'],
            'ssh_status': ['exact'],
            'https_status': ['exact'],
            'credential': ['exact'],
            'secret': ['exact'],
            'token': ['exact'],
            'certificate': ['exact'],
        }
