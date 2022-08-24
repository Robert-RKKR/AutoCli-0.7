# Rest framework import:
from rest_framework import serializers

# Base serializer import:
from network.all.base_api.base_serializer import BaseSerializer

# Model import:
from network.inventory.models.credential import Credential


# Serializer class:
class SimpleCredentialSerializer(BaseSerializer):

    # Object URL definition:
    url = serializers.HyperlinkedIdentityField(
        view_name='api-inventory:credential-detail',
        read_only=False,
    )

    class Meta:

        model = Credential
        fields = [
            'pk',
            'url',
            'root',
            'active',
            'created',
            'updated',
            'name',
            'description',
            'password',
        ]
        read_only_fields = [
            'root',
            'created',
            'updated',
        ]
