# Rest framework import:
from rest_framework import viewsets

# Paginator import:
from network.all.base_api.base_pagination import BaseSmallPaginator

# Model import:
from network.inventory.models.credential import Credential

# Serializer import:
from ..serializers.simple_credential import SimpleCredentialSerializer
from ..serializers.credential import CredentialSerializer

# Base mode view set import:
from network.all.base_api.base_modelviewset import BaseModelViewSet


# ViewSet model classes:
class CredentialView(BaseModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = Credential.objects.all()
    pagination_class = BaseSmallPaginator
    # Serializer classes:
    serializer_class = CredentialSerializer
    single_serializer_class = SimpleCredentialSerializer


class SimpleCredentialView(BaseModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = Credential.objects.all()
    serializer_class = SimpleCredentialSerializer
    pagination_class = BaseSmallPaginator
