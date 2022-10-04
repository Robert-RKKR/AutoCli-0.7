# Rest framework import:
from rest_framework.serializers import HyperlinkedIdentityField

# Base serializer import:
from network.all.base_api.base_serializer import BaseSerializer

# Models import:
from network.updates.models.snapshot import Snapshot


# Serializer class:
class SnapshotSerializer(BaseSerializer):

    # Object URL definition:
    url = HyperlinkedIdentityField(
        view_name='api-updates:snapshot-detail',
        read_only=False,
    )

    class Meta:

        model = Snapshot
        fields = BaseSerializer.base_fields + [
            'name',
            'description',
        ]
