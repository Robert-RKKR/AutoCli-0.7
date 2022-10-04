# Rest framework import:
from rest_framework.serializers import HyperlinkedIdentityField

# Base serializer import:
from messages.all.base_api.base_serializer import BaseSerializer

# Models import:
from messages.notifications.models.notification import Notification


# Serializer class:
class NotificationSerializer(BaseSerializer):

    # Object URL definition:
    url = HyperlinkedIdentityField(
        view_name='api-notifications:notifications-detail',
        read_only=False,
    )

    class Meta:

        model = Notification
        fields = BaseSerializer.base_fields + [
            'type',
            'application',
            'message',
        ]
