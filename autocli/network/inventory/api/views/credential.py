# Rest framework import:
from rest_framework.authentication import SessionAuthentication
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import DjangoModelPermissions

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
    # Authentication and permissions:
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [DjangoModelPermissions]


class SimpleCredentialView(BaseModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = Credential.objects.all()
    serializer_class = SimpleCredentialSerializer
    pagination_class = BaseSmallPaginator
    # Authentication and permissions:
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [DjangoModelPermissions]
