# Base filter import:
from messages.all.base_model.filters.base_filter import BaseFilter

# Model import:
from messages.logger.models.log import Log


# Filters:
class LogFilter(BaseFilter):

    class Meta:

        model = Log
        fields = {
            'id': ['exact', 'icontains'],
            'app_name': ['exact', 'icontains'],
            'model_name': ['exact', 'icontains'],
            'application': ['exact', 'icontains'],
            'severity': ['exact', 'icontains'],
            'message': ['exact', 'icontains'],
            'execution': ['exact', 'icontains', 'gt', 'lt'],
            'code_id': ['exact'],
            'task_id': ['exact'],
        }

