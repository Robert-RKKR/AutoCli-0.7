# Base filter import:
from messages.all.base_model.filters.base_filter import BaseFilter

# Model import:
from messages.changes.models.change_log import ChangeLog


# Filters:
class ChangeLogFilter(BaseFilter):

    class Meta:

        model = ChangeLog
        fields = {
            'id': ['exact', 'icontains'],
            'app_name': ['exact', 'icontains'],
            'model_name': ['exact', 'icontains'],
            'object_id': ['exact'],
        }

