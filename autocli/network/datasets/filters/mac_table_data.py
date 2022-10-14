# Base filter import:
from network.all.base_model.filters.base_filter import BaseFilter

# Model import:
from network.datasets.models.mac_table_data import MacTableData


# Filters:
class MacTableDataFilter(BaseFilter):

    class Meta:

        model = MacTableData
        fields = {
            'id': ['exact', 'icontains'],
            'active': ['exact'],
            'XXX': ['exact', 'icontains'],
        }
