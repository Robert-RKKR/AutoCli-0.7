# Base filter import:
from network.all.base_model.filters.base_filter import BaseFilter

# Model import:
from network.datasets.models.environment_data import EnvironmentData


# Filters:
class EnvironmentDataFilter(BaseFilter):

    class Meta:

        model = EnvironmentData
        fields = {
            'id': ['exact', 'icontains'],
            'active': ['exact'],
            'XXX': ['exact', 'icontains'],
        }
