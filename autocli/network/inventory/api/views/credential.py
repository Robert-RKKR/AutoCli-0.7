# Paginator import:
from network.all.base_api.base_pagination import BaseSmallPaginator

# Model import:
from network.inventory.models.credential import Credential

# Serializer import:
from ..serializers.simple_credential import SimpleCredentialSerializer
from ..serializers.credential import CredentialSerializer

# Base mode view set import:
from network.all.base_api.base_modelviewset import BaseModelViewSet

# Filter set class import:
from network.inventory.filters.credential import CredentialFilter


# ViewSet model classes:
class CredentialView(BaseModelViewSet):
    """
    A ViewSet for viewing and editing object/s.
    """
    # Basic API view parameters:
    queryset = Credential.objects.all()
    pagination_class = BaseSmallPaginator
    # Serializer classes:
    serializer_class = CredentialSerializer
    single_serializer_class = SimpleCredentialSerializer
    # Django rest framework filters:
    filterset_class = CredentialFilter
    search_fields = BaseModelViewSet.base_search_fields + [
        'name',
        'description',
        'username',
    ]
    ordering_fields = BaseModelViewSet.base_ordering_fields + [
        'name',
        'hostname',
        'username',
    ]


class SimpleCredentialView(BaseModelViewSet):
    """
    A simple ViewSet for viewing and editing object/s.
    """
    # Execute API view from Swagger schema:
    exclude_from_schema = True
    swagger_schema = None
    # Basic API view parameters:
    queryset = Credential.objects.all()
    pagination_class = BaseSmallPaginator
    # Serializer classes:
    serializer_class = SimpleCredentialSerializer
    # Django rest framework filters:
    filterset_class = CredentialFilter
    search_fields = BaseModelViewSet.base_search_fields + [
        'name',
        'description',
        'username',
    ]
    ordering_fields = BaseModelViewSet.base_ordering_fields + [
        'name',
        'hostname',
        'username',
    ]
