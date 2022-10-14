# Rest framework import:
from rest_framework.serializers import HyperlinkedIdentityField

# Base serializer import:
from network.all.base_api.base_serializer import BaseSerializer

# Models import:
from network.datasets.models.XXX import XXX

# Other serializer import:
from network.updates.models.update import UpdateSerializer


# Serializer class:
class Serializer(BaseSerializer):

    # Object URL definition:
    url = HyperlinkedIdentityField(
        view_name='api-updates:collected_data-detail',
        read_only=False,
    )
    # Object relation definition:
    update = UpdateSerializer(
        many=False,
        read_only=True,
    )

    class Meta:

        model = XXX
        fields = BaseSerializer.base_fields + [
            'update',
            'XXX',
        ]
