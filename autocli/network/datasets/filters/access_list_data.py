# Base filter import:
from network.all.base_model.filters.base_filter import BaseFilter

# Model import:
from network.datasets.models.access_list_data import AccessListData


# Filters:
class AccessListDataFilter(BaseFilter):

    class Meta:

        model = AccessListData
        fields = {
            'id': ['exact', 'icontains'],
            'active': ['exact'],
            'XXX': ['exact', 'icontains'],
        }
