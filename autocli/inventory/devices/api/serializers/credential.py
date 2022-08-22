# Base serializer import:
from inventory.all.base_api.base_serializer import BaseSerializer

# Model import:
from inventory.devices.models.credential import Credential


# Serializer class:
class CredentialSerializer(BaseSerializer):

    class Meta:

        model = Credential
        fields = ['name', 'username', 'password']
