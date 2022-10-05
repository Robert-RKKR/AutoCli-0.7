# Base filter import:
from network.all.base_model.filters.base_filter import BaseFilter

# Model import:
from network.updates.models.collected_data import CollectedData


# Filters:
class CollectedDataFilter(BaseFilter):

    class Meta:

        model = CollectedData
        fields = {
            'id': ['exact', 'icontains'],
            'active': ['exact'],
            'result_status': ['exact'],
            'raw_data_status': ['exact'],
            'processed_data_status': ['exact'],
            'command_name': ['exact', 'icontains'],
            'command_raw_data': ['exact', 'icontains']
        }
