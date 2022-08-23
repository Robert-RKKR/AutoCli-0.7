# Rest framework import:
from rest_framework import serializers

# Base serializer import:
from network.all.base_api.base_serializer import BaseSerializer

# Model import:
from network.inventory.models.credential import Credential
from network.inventory.models.device import Device

# Other serializer import:
from .device_simple import SimpleDeviceSerializer


# Serializer class:
class CredentialSerializer(BaseSerializer):

    url = serializers.HyperlinkedIdentityField(
        view_name='api-inventory:credential-detail'
    )
    devices = SimpleDeviceSerializer(
        many=True,
        read_only=True,
    )

    class Meta:

        model = Credential
        fields = [
            'pk',
            'url',
            'root',
            'active',
            'created',
            'updated',
            'name',
            'description',
            'password',
            'devices',
        ]
        read_only_fields = [
            'root',
            'created',
            'updated',
        ]
