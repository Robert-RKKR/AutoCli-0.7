# Base filter import:
from network.all.base_model.filters.base_filter import BaseFilter

# Model import:
from network.datasets.models.etherchannel_data import EtherchannelData


# Filters:
class EtherchannelDataFilter(BaseFilter):

    class Meta:

        model = EtherchannelData
        fields = {
            'id': ['exact', 'icontains'],
            'active': ['exact'],
            'XXX': ['exact', 'icontains'],
        }
