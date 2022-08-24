# Rest framework import:
from rest_framework import serializers

# Base serializer import:
from network.all.base_api.base_serializer import BaseSerializer

# Model import:
from network.inventory.models.device_type import DeviceType

# Other serializer import:
from .simple_device import SimpleDeviceSerializer


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
    # devices = serializers.HyperlinkedRelatedField(
    #     many=True,
    #     read_only=True,
    #     view_name='api-inventory:device-detail',
    # )

    class Meta:

        model = DeviceType
        fields = [
            'pk',
            'url',
            'root',
            'active',
            'created',
            'updated',
            'name',
            'description',
            'netmiko_name',
            'devices',
        ]
        read_only_fields = [
            'root',
            'created',
            'updated',
        ]
