# Rest framework import:
from rest_framework import serializers

# Base serializer import:
from network.all.base_api.base_serializer import BaseSerializer

# Model import:
from network.inventory.models.group import Group

# Other serializer import:
from .simple_device import SimpleDeviceSerializer
from .simple_credential import SimpleCredentialSerializer


# Serializer class:
class GroupSerializer(BaseSerializer):

    # Object URL definition:
    url = serializers.HyperlinkedIdentityField(
        view_name='api-inventory:group-detail',
        read_only=False,
    )
    # Object relation definition:
    credential = SimpleCredentialSerializer(
        many=False,
        read_only=True,
        required=False,
    )
    devices = SimpleDeviceSerializer(
        many=True,
        read_only=True,
        required=False,
    )
    root_folder = serializers.StringRelatedField(
        many=False
    )

    class Meta:

        model = Group
        fields = BaseSerializer.base_fields + [
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
        read_only_fields = BaseSerializer.base_read_only_fields
