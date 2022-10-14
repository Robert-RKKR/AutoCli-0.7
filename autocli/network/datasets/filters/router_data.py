# Base filter import:
from network.all.base_model.filters.base_filter import BaseFilter

# Model import:
from network.datasets.models.router_data import RouterData


# Filters:
class RouterDataFilter(BaseFilter):

    class Meta:

        model = RouterData
        fields = {
            'id': ['exact', 'icontains'],
            'active': ['exact'],
        }
