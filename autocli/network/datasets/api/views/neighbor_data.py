# Models import:
from network.datasets.models.neighbor_data import NeighborData

# Serializer import:
from ..serializers.neighbor_data import NeighborDataSerializer

# Paginator import:
from network.all.base_api.base_pagination import BaseSmallPaginator

# Base mode view set import:
from network.all.base_api.base_modelviewset import BaseRoModelViewSet

# Filter import:
from network.datasets.filters.neighbor_data import NeighborDataFilter


# ViewSet model classes:
class NeighborDataView(BaseRoModelViewSet):
    """
    A ViewSet for viewing and editing object/s.
    """
    # Basic API view parameters:
    queryset = NeighborData.objects.all()
    pagination_class = BaseSmallPaginator
    # Serializer classes:
    serializer_class = NeighborDataSerializer
    # Django rest framework filters:
    filterset_class = NeighborDataFilter
    ordering_fields = BaseRoModelViewSet.base_ordering_fields + [
        'update',
    ]
