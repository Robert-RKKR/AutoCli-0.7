# Base filter import:
from network.all.base_model.filters.base_filter import BaseFilter

# Model import:
from network.inventory.models.device_type import DeviceType


# Filters:
class DeviceTypeFilter(BaseFilter):

    class Meta:

        model = DeviceType
        fields = {
            'id': ['exact', 'icontains'],
            'active': ['exact'],
            'name': ['exact', 'icontains'],
            'description': ['exact', 'icontains'],
            'netmiko_name': ['exact', 'icontains'],
        }
