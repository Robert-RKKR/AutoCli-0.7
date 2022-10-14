# Rest framework import:
from rest_framework.serializers import HyperlinkedIdentityField

# Base serializer import:
from network.all.base_api.base_serializer import BaseSerializer

# Models import:
from network.updates.models.update import Update

# Other serializer import:
from network.inventory.api.serializers.simple_device import SimpleDeviceSerializer
from network.updates.api.serializers.snapshot import SnapshotSerializer


# Serializer class:
class UpdateSerializer(BaseSerializer):

    # Object URL definition:
    url = HyperlinkedIdentityField(
        view_name='api-updates:update-detail',
        read_only=False,
    )
    # Object relation definition:
    device = SimpleDeviceSerializer(
        many=False,
        read_only=True,
    )
    # Object relation definition:
    snapshot = SnapshotSerializer(
        many=False,
        read_only=True,
    )

    class Meta:

        model = Update
        fields = BaseSerializer.base_fields + [
            'device',
            'snapshot',
            'status',
            'result_status',
            'correlated',
        ]
