# Rest framework import:
from rest_framework.serializers import HyperlinkedIdentityField

# Base serializer import:
from network.all.base_api.base_serializer import BaseSerializer

# Models import:
from network.datasets.models.etherchannel_data import EtherchannelData

# Other serializer import:
from network.updates.api.serializers.update import UpdateSerializer


# Serializer class:
class EtherchannelDataSerializer(BaseSerializer):

    # Object URL definition:
    url = HyperlinkedIdentityField(
        view_name='api-datasets:etherchannel_data-detail',
        read_only=False,
    )
    # Object relation definition:
    update = UpdateSerializer(
        many=False,
        read_only=True,
    )

    class Meta:

        model = EtherchannelData
        fields = BaseSerializer.base_fields + [
            'update',
        ]
