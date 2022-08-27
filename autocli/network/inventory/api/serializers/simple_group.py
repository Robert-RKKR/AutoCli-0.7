# Rest framework import:
from rest_framework import serializers

# Base serializer import:
from network.all.base_api.base_serializer import BaseSerializer

# Model import:
from network.inventory.models.credential import Credential
from network.inventory.models.device import Device
from network.inventory.models.group import Group

# Other serializer import:
from .simple_device import SimpleDeviceSerializer


# Serializer class:
class SimpleGroupSerializer(BaseSerializer):

    # Object URL definition:
    url = serializers.HyperlinkedIdentityField(
        view_name='api-inventory:group-detail',
        read_only=False,
    )
    # Object relation definition:
    credential = serializers.PrimaryKeyRelatedField(
        queryset=Credential.objects.all(),
        required=False,
    )
    devices_id = serializers.PrimaryKeyRelatedField(
        queryset=Device.objects.all(),
        source='devices',
        many=True,
        read_only=False,
        required=False,
    )
    root_folder = serializers.PrimaryKeyRelatedField(
        queryset=Group.objects.all(),
        required=False,
    )

    class Meta:

        model = Group
        fields = BaseSerializer.base_fields + [
            'name',
            'description',
            'root_folder',
            'devices_id',
            'ssh_port',
            'https_port',
            'credential',
            'secret',
            'token',
            'certificate',
        ]
        read_only_fields = BaseSerializer.base_read_only_fields
