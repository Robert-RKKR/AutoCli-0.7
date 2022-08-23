# Rest framework import:
from rest_framework import viewsets

# Model import:
from network.inventory.models.credential import Credential

# Serializer import:
from ..serializers.credential import CredentialSerializer


class CredentialView(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = Credential.objects.all()
    serializer_class = CredentialSerializer
