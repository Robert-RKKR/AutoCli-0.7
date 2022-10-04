# Rest framework import:
from rest_framework.serializers import HyperlinkedIdentityField

# Base serializer import:
from messages.all.base_api.base_serializer import BaseSerializer

# Models import:
from messages.changes.models.change_log import ChangeLog


# Serializer class:
class ChangeLogSerializer(BaseSerializer):

    # Object URL definition:
    url = HyperlinkedIdentityField(
        view_name='api-changes:change_log-detail',
        read_only=False,
    )

    class Meta:

        model = ChangeLog
        fields = BaseSerializer.base_fields + [
            'object_representation',
            'administrator',
            'action',
            'after',
        ]
