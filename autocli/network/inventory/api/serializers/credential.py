# Rest framework import:
from rest_framework import serializers

# Base serializer import:
from network.all.base_api.base_serializer import BaseSerializer

# Model import:
from network.inventory.models.credential import Credential

# Other serializer import:
from .simple_device import SimpleDeviceSerializer


# Serializer class:
class CredentialSerializer(BaseSerializer):

    # Object URL definition:
    url = serializers.HyperlinkedIdentityField(
        view_name='api-inventory:credential-detail',
        read_only=False,
    )
    # Object relation definition:
    devices = SimpleDeviceSerializer(
        many=True,
        read_only=True,
    )

    class Meta:

        model = Credential
        fields = BaseSerializer.base_fields + [
            'name',
            'username',
            'description',
            'password',
            'devices',
        ]
        read_only_fields = BaseSerializer.base_read_only_fields
