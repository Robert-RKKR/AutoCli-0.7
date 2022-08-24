# Rest framework import:
from rest_framework import viewsets

# Paginator import:
from network.all.base_api.base_pagination import BaseSmallPaginator

# Model import:
from network.inventory.models.credential import Credential

# Serializer import:
from ..serializers.simple_credential import SimpleCredentialSerializer
from ..serializers.credential import CredentialSerializer


class CredentialView(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = Credential.objects.all()
    serializer_class = CredentialSerializer
    pagination_class = BaseSmallPaginator


class SimpleCredentialView(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = Credential.objects.all()
    serializer_class = SimpleCredentialSerializer
    pagination_class = BaseSmallPaginator
