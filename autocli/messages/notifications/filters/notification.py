# Base filter import:
from messages.all.base_model.filters.base_filter import BaseFilter

# Model import:
from messages.notifications.models.notification import Notification


# Filters:
class NotificationFilter(BaseFilter):

    class Meta:

        model = Notification
        fields = {
            'id': ['exact', 'icontains'],
            'app_name': ['exact', 'icontains'],
            'model_name': ['exact', 'icontains'],
            'object_id': ['exact'],
            'application': ['exact', 'icontains'],
            'message': ['exact', 'icontains']
        }

