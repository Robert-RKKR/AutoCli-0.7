# Rest framework import:
from rest_framework import serializers

# Base serializer import:
from network.all.base_api.base_serializer import BaseSerializer

# Model import:
from network.inventory.models.device_type import DeviceType


# Serializer class:
class DeviceTypeSerializer(BaseSerializer):

    url = serializers.HyperlinkedIdentityField(
        view_name='api-inventory:device_type-detail'
    )

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
        ]
        read_only_fields = [
            'root',
            'created',
            'updated',
        ]
