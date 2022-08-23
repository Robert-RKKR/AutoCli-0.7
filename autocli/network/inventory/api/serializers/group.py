# Rest framework import:
from rest_framework import serializers

# Base serializer import:
from network.all.base_api.base_serializer import BaseSerializer

# Model import:
from network.inventory.models.group import Group

# Other serializer import:
from .credential import CredentialSerializer

# Other serializer import:
from .device_simple import SimpleDeviceSerializer


# Serializer class:
class GroupSerializer(BaseSerializer):

    url = serializers.HyperlinkedIdentityField(
        view_name='api-inventory:group-detail'
    )
    credential = CredentialSerializer(
        many=False,
        read_only=True,
    )
    devices = SimpleDeviceSerializer(
        many=True,
        read_only=True,
    )
    root_folder = serializers.StringRelatedField(many=False)

    class Meta:

        model = Group
        fields = [
            'pk',
            'url',
            'root',
            'active',
            'created',
            'updated',
            'name',
            'description',
            'root_folder',
            'devices',
            'ssh_port',
            'https_port',
            'credential',
            'secret',
            'token',
            'certificate',
        ]
        read_only_fields = [
            'root',
            'created',
            'updated',
        ]
