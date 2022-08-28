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
    A ViewSet for viewing and editing object/s.
    """
    queryset = Credential.objects.all()
    pagination_class = BaseSmallPaginator
    # Serializer classes:
    serializer_class = CredentialSerializer
    single_serializer_class = SimpleCredentialSerializer
    # Django rest framework filters:


class SimpleCredentialView(BaseModelViewSet):
    """
    A simple ViewSet for viewing and editing object/s.
    """
    queryset = Credential.objects.all()
    serializer_class = SimpleCredentialSerializer
    pagination_class = BaseSmallPaginator
    # Django rest framework filters:
