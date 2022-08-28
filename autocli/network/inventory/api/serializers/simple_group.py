# Rest framework import:
from rest_framework.serializers import HyperlinkedIdentityField
from rest_framework.serializers import PrimaryKeyRelatedField

# Base serializer import:
from network.all.base_api.base_serializer import BaseSerializer

# Model import:
from network.inventory.models.credential import Credential
from network.inventory.models.device import Device
from network.inventory.models.group import Group


# Serializer class:
class SimpleGroupSerializer(BaseSerializer):

    # Object URL definition:
    url = HyperlinkedIdentityField(
        view_name='api-inventory:group-detail',
        read_only=False,
    )
    # Object relation definition:
    credential = PrimaryKeyRelatedField(
        queryset=Credential.objects.all(),
        required=False,
        allow_null=True,
    )
    devices_id = PrimaryKeyRelatedField(
        queryset=Device.objects.all(),
        source='devices',
        many=True,
        read_only=False,
        required=False,
        allow_null=True,
    )
    root_folder = PrimaryKeyRelatedField(
        queryset=Group.objects.all(),
        required=False,
        allow_null=True,
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
