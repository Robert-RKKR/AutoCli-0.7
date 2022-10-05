# Base filter import:
from network.all.base_model.filters.base_filter import BaseFilter

# Model import:
from network.updates.models.snapshot import Snapshot


# Filters:
class SnapshotFilter(BaseFilter):

    class Meta:

        model = Snapshot
        fields = {
            'id': ['exact', 'icontains'],
            'active': ['exact'],
        }
