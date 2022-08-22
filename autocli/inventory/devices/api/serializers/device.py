# Rest framework import:
from rest_framework import serializers

# Base serializer import:
from inventory.all.base_api.base_serializer import BaseSerializer

# other serializer import:
from .credential import CredentialSerializer

# Model import:
from inventory.devices.models.device import Device


# Serializer class:
class DeviceSerializer(BaseSerializer):

    credential = CredentialSerializer(
        many=False,
        read_only=True
    )

    class Meta:

        model = Device
        fields = ['active', 'name', 'hostname', 'credential']
