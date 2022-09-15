# Rest framework import:
from rest_framework.serializers import HyperlinkedIdentityField

# Base serializer import:
from network.all.base_api.base_serializer import BaseSerializer

# Models import:
from network.updates.models.collected_data import CollectedData

# Other serializer import:
from .update import UpdateSerializer


# Serializer class:
class CollectedDataSerializer(BaseSerializer):

    # Object URL definition:
    url = HyperlinkedIdentityField(
        view_name='api-updates:collected_data',
        read_only=False,
    )
    # Object relation definition:
    update = UpdateSerializer(
        many=False,
        read_only=True,
    )

    class Meta:

        model = CollectedData
        fields = BaseSerializer.base_fields + [
            'update',
            'result_status',
            'raw_data_status',
            'processed_data_status',
            'command_name',
            'command_raw_data',
            'command_processed_data',
        ]
