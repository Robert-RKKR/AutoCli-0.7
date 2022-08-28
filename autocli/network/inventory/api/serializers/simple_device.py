# Rest framework import:
from rest_framework.serializers import HyperlinkedIdentityField
from rest_framework.serializers import PrimaryKeyRelatedField

# Base serializer import:
from network.all.base_api.base_serializer import BaseSerializer

# Model import:
from network.inventory.models.device_type import DeviceType
from network.inventory.models.credential import Credential
from network.inventory.models.device import Device


# Serializer class:
class SimpleDeviceSerializer(BaseSerializer):

    # Object URL definition:
    url = HyperlinkedIdentityField(
        view_name='api-inventory:device-detail',
        read_only=False,
    )
    # Object relation definition:
    device_type = PrimaryKeyRelatedField(
        queryset=DeviceType.objects.all(),
        required=False,
        allow_null=True,
        help_text='Type of network device system.',
    )
    credential = PrimaryKeyRelatedField(
        queryset=Credential.objects.all(),
        required=False,
        allow_null=True,
        help_text='Credential needed to establish SSH / HTTPS connection.',
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
        read_only_fields = BaseSerializer.base_read_only_fields + [
            'ssh_status',
            'https_status',
        ]
