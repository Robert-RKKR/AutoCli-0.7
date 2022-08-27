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
        read_only=True,
    )
    credential = SimpleCredentialSerializer(
        many=False,
        read_only=True,
    )

    class Meta:

        model = Device
        fields = BaseSerializer.base_fields + [
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
        read_only_fields = BaseSerializer.base_read_only_fields
