# Rest framework import:
from rest_framework import serializers

# Base serializer import:
from network.all.base_api.base_serializer import BaseSerializer

# Model import:
from network.inventory.models.group import Group


# Serializer class:
class SimpleGroupSerializer(BaseSerializer):

    # Object URL definition:
    url = serializers.HyperlinkedIdentityField(
        view_name='api-inventory:group-detail',
        read_only=False,
    )
    # Object relation definition:
    credential = serializers.StringRelatedField(
        many=False,
        read_only=True,
    )
    devices = serializers.StringRelatedField(
        many=False,
        read_only=True,
    )
    root_folder = serializers.StringRelatedField(
        many=False,
        read_only=True,
    )

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
