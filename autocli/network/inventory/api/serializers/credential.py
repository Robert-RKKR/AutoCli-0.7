# Base serializer import:
from network.all.base_api.base_serializer import BaseSerializer

# Model import:
from network.inventory.models.credential import Credential


# Serializer class:
class CredentialSerializer(BaseSerializer):

    class Meta:

        model = Credential
        fields = ['name', 'username', 'password']
