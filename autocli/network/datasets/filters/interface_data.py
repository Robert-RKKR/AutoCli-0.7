# Base filter import:
from network.all.base_model.filters.base_filter import BaseFilter

# Model import:
from network.datasets.models.interface_data import InterfaceData


# Filters:
class InterfaceDataFilter(BaseFilter):

    class Meta:

        model = InterfaceData
        fields = {
            'id': ['exact', 'icontains'],
            'active': ['exact'],
        }
