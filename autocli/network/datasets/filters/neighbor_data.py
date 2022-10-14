# Base filter import:
from network.all.base_model.filters.base_filter import BaseFilter

# Model import:
from network.datasets.models.neighbor_data import NeighborData


# Filters:
class NeighborDataFilter(BaseFilter):

    class Meta:

        model = NeighborData
        fields = {
            'id': ['exact', 'icontains'],
            'active': ['exact'],
            'XXX': ['exact', 'icontains'],
        }
