# Base filter import:
from network.all.base_model.filters.base_filter import BaseFilter

# Model import:
from network.datasets.models.dmvpn_data import DmvpnData


# Filters:
class DmvpnDataFilter(BaseFilter):

    class Meta:

        model = DmvpnData
        fields = {
            'id': ['exact', 'icontains'],
            'active': ['exact'],
        }
