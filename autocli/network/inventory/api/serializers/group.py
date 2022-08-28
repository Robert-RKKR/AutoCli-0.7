# Rest framework import:
from rest_framework.serializers import HyperlinkedIdentityField
from rest_framework.serializers import StringRelatedField

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
    url = HyperlinkedIdentityField(
        view_name='api-inventory:group-detail',
        read_only=False,
    )
    # Object relation definition:
    credential = SimpleCredentialSerializer(
        many=False,
        read_only=True,
    )
    devices = SimpleDeviceSerializer(
        many=True,
        read_only=True,
    )
    root_folder = StringRelatedField(
        many=False,
        read_only=True,
    )
    child_folders = StringRelatedField(
        many=True,
        read_only=True,
    )

    class Meta:

        model = Group
        fields = BaseSerializer.base_fields + [
            'name',
            'description',
            'ssh_port',
            'https_port',
            'secret',
            'token',
            'certificate',
            'credential',
            'devices',
            'root_folder',
            'child_folders',
        ]
        read_only_fields = BaseSerializer.base_read_only_fields
