# Rest framework import:
from rest_framework.serializers import HyperlinkedIdentityField

# Base serializer import:
from network.all.base_api.base_serializer import BaseSerializer

# Model import:
from network.inventory.models.device_type import DeviceType


# Serializer class:
class SimpleDeviceTypeSerializer(BaseSerializer):

    # Object URL definition:
    url = HyperlinkedIdentityField(
        view_name='api-inventory:device_type-detail',
        read_only=False,
    )

    class Meta:

        model = DeviceType
        fields = BaseSerializer.base_fields + [
            'name',
            'description',
            'netmiko_name',
        ]
        read_only_fields = BaseSerializer.base_read_only_fields
