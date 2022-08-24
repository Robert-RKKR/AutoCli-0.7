# Rest framework import:
from rest_framework import serializers

# Base serializer import:
from network.all.base_api.base_serializer import BaseSerializer

# Model import:
from network.inventory.models.device import Device

# Other serializer import:
from .simple_device_type import SimpleDeviceTypeSerializer
from .simple_credential import SimpleCredentialSerializer


# Serializer class:
class DeviceSerializer(BaseSerializer):

    # Object URL definition:
    url = serializers.HyperlinkedIdentityField(
        view_name='api-inventory:device-detail',
        read_only=False,
    )
    # Object relation definition:
    device_type = SimpleDeviceTypeSerializer(
        many=False,
        required=False,
    )
    credential = SimpleCredentialSerializer(
        many=False,
        required=False,
    )

    class Meta:

        model = Device
        fields = [
            'pk',
            'url',
            'root',
            'active',
            'created',
            'updated',
            'name',
            'description',
            'hostname',
            'ssh_port',
            'https_port',
            'device_type',
            'ssh_status',
            'https_status',
            'credential',
            'secret',
            'token',
            'certificate',
        ]
        read_only_fields = [
            'root',
            'created',
            'updated',
            'ssh_status',
            'https_status',
        ]
