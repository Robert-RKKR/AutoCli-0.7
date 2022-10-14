# Base filter import:
from network.all.base_model.filters.base_filter import BaseFilter

# Model import:
from network.datasets.models.nhrp_data import NhrpData


# Filters:
class NhrpDataFilter(BaseFilter):

    class Meta:

        model = NhrpData
        fields = {
            'id': ['exact', 'icontains'],
            'active': ['exact'],
            'XXX': ['exact', 'icontains'],
        }
