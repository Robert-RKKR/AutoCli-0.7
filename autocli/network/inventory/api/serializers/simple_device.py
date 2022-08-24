# Rest framework import:
from rest_framework import serializers

# Base serializer import:
from network.all.base_api.base_serializer import BaseSerializer

# Model import:
from network.inventory.models.device_type import DeviceType
from network.inventory.models.credential import Credential
from network.inventory.models.device import Device


# Serializer class:
class SimpleDeviceSerializer(BaseSerializer):

    # Object URL definition:
    url = serializers.HyperlinkedIdentityField(
        view_name='api-inventory:device-detail',
        read_only=False,
    )
    # Object relation definition:
    # credential = serializers.StringRelatedField(
    #     many=False,
    #     read_only=False,
    # )
    # device_type = serializers.StringRelatedField(
    #     many=False,
    #     read_only=False,
    # )
    credential = serializers.PrimaryKeyRelatedField(
        queryset=Credential.objects.all()
    )
    device_type = serializers.PrimaryKeyRelatedField(
        queryset=DeviceType.objects.all()
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
