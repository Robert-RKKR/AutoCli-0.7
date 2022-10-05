# Base filter import:
from network.all.base_model.filters.base_filter import BaseFilter

# Model import:
from network.inventory.models.device import Device


# Filters:
class DeviceFilter(BaseFilter):

    class Meta:

        model = Device
        fields = {
            'id': ['exact', 'icontains'],
            'active': ['exact'],
            'name': ['exact', 'icontains'],
            'description': ['exact', 'icontains'],
            'hostname': ['exact', 'icontains'],
            'ssh_port': ['exact', 'icontains', 'lt', 'gt'],
            'https_port': ['exact', 'icontains', 'lt', 'gt'],
            'device_type': ['exact'],
            'ssh_status': ['exact'],
            'https_status': ['exact'],
            'credential': ['exact'],
            'token': ['exact'],
            'certificate': ['exact'],
        }
