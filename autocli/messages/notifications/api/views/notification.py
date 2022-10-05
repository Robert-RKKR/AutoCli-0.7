# Rest Django import:
from rest_framework import generics

# Models import:
from messages.notifications.models.notification import Notification

# Serializer import:
from messages.notifications.api.serializers.notification import NotificationSerializer

# Paginator import:
from messages.all.base_api.base_pagination import BaseMediumPaginator

# Base mode view set import:
from messages.all.base_api.base_modelviewset import BaseRoModelViewSet

# Filter import:
from messages.notifications.filters.notification import NotificationFilter


# ViewSet model classes:
class NotificationView(BaseRoModelViewSet):
    """
    A ViewSet for viewing and editing object/s.
    """
    # Basic API view parameters:
    queryset = Notification.objects.all()
    pagination_class = BaseMediumPaginator
    # Serializer classes:
    serializer_class = NotificationSerializer
    # Django rest framework filters:
    filterset_class = NotificationFilter
    search_fields = BaseRoModelViewSet.base_search_fields + [
        'message'
    ]
    ordering_fields = BaseRoModelViewSet.base_ordering_fields + [
        'app_name',
        'model_name',
        'application'
    ]
