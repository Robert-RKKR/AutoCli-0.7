# Rest Django import:
from rest_framework import generics

# Models import:
from messages.notifications.models.notification import Notification

# Serializer import:
from messages.notifications.api.serializers.notification import NotificationSerializer

# Paginator import:
from messages.all.base_api.base_pagination import BaseMediumPaginator


# All Change Log views:
class NotificationListAPI(generics.ListAPIView):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    pagination_class = BaseMediumPaginator


class NotificationRetrieveAPI(generics.RetrieveAPIView):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
