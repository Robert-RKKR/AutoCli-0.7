# Rest framework import:
from rest_framework.serializers import HyperlinkedIdentityField

# Base serializer import:
from network.all.base_api.base_serializer import BaseSerializer

# Model import:
from network.inventory.models.credential import Credential


# Serializer class:
class SimpleCredentialSerializer(BaseSerializer):

    # Object URL definition:
    url = HyperlinkedIdentityField(
        view_name='api-inventory:credential-detail',
        read_only=False,
    )

    class Meta:

        model = Credential
        fields = BaseSerializer.base_fields + [
            'name',
            'username',
            'description',
            'password',
        ]
        read_only_fields = BaseSerializer.base_read_only_fields
