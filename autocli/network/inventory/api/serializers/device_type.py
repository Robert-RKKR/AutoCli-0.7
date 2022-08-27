# Rest framework import:
from rest_framework import serializers

# Base serializer import:
from network.all.base_api.base_serializer import BaseSerializer

# Model import:
from network.inventory.models.device_type import DeviceType

# Other serializer import:
from .simple_device import SimpleDeviceSerializer
from .simple_device_type_template import SimpleDeviceTypeTemplateSerializer


# Serializer class:
class DeviceTypeSerializer(BaseSerializer):

    # Object URL definition:
    url = serializers.HyperlinkedIdentityField(
        view_name='api-inventory:device_type-detail',
        read_only=False,
    )
    # Object relation definition:
    devices = SimpleDeviceSerializer(
        many=True,
        read_only=True,
    )
    device_type_templates = SimpleDeviceTypeTemplateSerializer(
        many=True,
        read_only=True,
    )

    class Meta:

        model = DeviceType
        fields = BaseSerializer.base_fields + [
            'name',
            'description',
            'netmiko_name',
            'devices',
            'device_type_templates',
        ]
        read_only_fields = BaseSerializer.base_read_only_fields
