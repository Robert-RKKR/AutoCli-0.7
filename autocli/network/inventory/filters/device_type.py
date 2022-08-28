# Base filter import:
from network.all.base_model.filters.base_filter import BaseFilter

# Model import:
from network.inventory.models.device_type import DeviceType


# Filters:
class DeviceTypeFilter(BaseFilter):

    class Meta:

        model = DeviceType
        fields = {
            'id': ['exact', 'contains'],
            'active': ['exact'],
            'name': ['exact', 'contains'],
            'description': ['exact', 'contains'],
            'netmiko_name': ['exact', 'contains'],
        }
