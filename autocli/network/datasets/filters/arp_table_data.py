# Base filter import:
from network.all.base_model.filters.base_filter import BaseFilter

# Model import:
from network.datasets.models.arp_table_data import ArpTableData


# Filters:
class ArpTableDataFilter(BaseFilter):

    class Meta:

        model = ArpTableData
        fields = {
            'id': ['exact', 'icontains'],
            'active': ['exact'],
        }
