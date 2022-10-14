# Rest framework import:
from rest_framework.serializers import HyperlinkedIdentityField

# Base serializer import:
from network.all.base_api.base_serializer import BaseSerializer

# Models import:
from network.datasets.models.access_list_data import AccessListData

# Other serializer import:
from network.updates.api.serializers.update import UpdateSerializer


# Serializer class:
class AccessListDataSerializer(BaseSerializer):

    # Object URL definition:
    url = HyperlinkedIdentityField(
        view_name='api-datasets:access_list_data-detail',
        read_only=False,
    )
    # Object relation definition:
    update = UpdateSerializer(
        many=False,
        read_only=True,
    )

    class Meta:

        model = AccessListData
        fields = BaseSerializer.base_fields + [
            'update',
            'XXX',
        ]
