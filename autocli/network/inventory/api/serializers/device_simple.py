# Rest framework import:
from rest_framework import serializers

# Base serializer import:
from network.all.base_api.base_serializer import BaseSerializer

# Model import:
from network.inventory.models.device import Device


# Serializer class:
class SimpleDeviceSerializer(BaseSerializer):

    credential = serializers.StringRelatedField(many=False)
    device_type = serializers.StringRelatedField(many=False)
    url = serializers.HyperlinkedIdentityField(
        view_name='api-inventory:device-detail'
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
