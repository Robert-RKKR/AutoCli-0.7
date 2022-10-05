# Base filter import:
from network.all.base_model.filters.base_filter import BaseFilter

# Model import:
from network.updates.models.update import Update


# Filters:
class UpdateFilter(BaseFilter):

    class Meta:

        model = Update
        fields = {
            'id': ['exact', 'icontains'],
            'active': ['exact'],
            'device': ['exact'],
            'snapshot': ['exact'],
            'status': ['exact'],
        }
