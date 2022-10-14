# Base filter import:
from network.all.base_model.filters.base_filter import BaseFilter

# Model import:
from network.datasets.models.module_data import ModuleData


# Filters:
class ModuleDataFilter(BaseFilter):

    class Meta:

        model = ModuleData
        fields = {
            'id': ['exact', 'icontains'],
            'active': ['exact'],
        }
