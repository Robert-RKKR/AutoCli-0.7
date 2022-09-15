# Rest framework import:
from rest_framework.serializers import HyperlinkedIdentityField

# Base serializer import:
from messages.all.base_api.base_serializer import BaseSerializer

# Models import:
from messages.logger.models.log import Log


# Serializer class:
class LogSerializer(BaseSerializer):

    # Object URL definition:
    url = HyperlinkedIdentityField(
        view_name='api-logger:log',
        read_only=False,
    )

    class Meta:

        model = Log
        fields = BaseSerializer.base_fields + [
            'application',
            'code_id',
            'task_id',
            'severity',
            'message',
            'execution',
        ]
