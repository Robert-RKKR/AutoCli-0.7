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
            'id': ['exact', 'contains'],
            'active': ['exact'],
            'name': ['exact', 'contains'],
            'description': ['exact', 'contains'],
            'hostname': ['exact', 'contains'],
            'ssh_port': ['exact', 'contains', 'lt', 'gt'],
            'https_port': ['exact', 'contains', 'lt', 'gt'],
            'device_type': ['exact'],
            'ssh_status': ['exact'],
            'https_status': ['exact'],
            'credential': ['exact'],
            'token': ['exact'],
            'certificate': ['exact'],
        }
