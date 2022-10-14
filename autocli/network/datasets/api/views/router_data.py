# Models import:
from network.datasets.models.router_data import RouterData

# Serializer import:
from ..serializers.router_data import RouterDataSerializer

# Paginator import:
from network.all.base_api.base_pagination import BaseSmallPaginator

# Base mode view set import:
from network.all.base_api.base_modelviewset import BaseRoModelViewSet

# Filter import:
from network.datasets.filters.router_data import RouterDataFilter


# ViewSet model classes:
class RouterDataView(BaseRoModelViewSet):
    """
    A ViewSet for viewing and editing object/s.
    """
    # Basic API view parameters:
    queryset = RouterData.objects.all()
    pagination_class = BaseSmallPaginator
    # Serializer classes:
    serializer_class = RouterDataSerializer
    # Django rest framework filters:
    filterset_class = RouterDataFilter
    search_fields = BaseRoModelViewSet.base_search_fields + [
        'XXX',
    ]
    ordering_fields = BaseRoModelViewSet.base_ordering_fields + [
        'update',
        'XXX',
    ]
