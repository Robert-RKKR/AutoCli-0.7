# Base filter import:
from network.all.base_model.filters.base_filter import BaseFilter

# Model import:
from network.datasets.models.device_data import DeviceData


# Filters:
class DeviceDataFilter(BaseFilter):

    class Meta:

        model = DeviceData
        fields = {
            'id': ['exact', 'icontains'],
            'active': ['exact'],
        }
