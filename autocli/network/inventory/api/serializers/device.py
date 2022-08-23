# Rest framework import:
from rest_framework import serializers

# Base serializer import:
from network.all.base_api.base_serializer import BaseSerializer

# Other serializer import:
from .device_type import DeviceTypeSerializer
from .credential import CredentialSerializer

# Model import:
from network.inventory.models.device import Device


# Serializer class:
class DeviceSerializer(BaseSerializer):

    url = serializers.HyperlinkedIdentityField(
        view_name='api-inventory:device-detail'
    )
    credential = CredentialSerializer(
        many=False
    )
    device_type = DeviceTypeSerializer(
        many=False
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
