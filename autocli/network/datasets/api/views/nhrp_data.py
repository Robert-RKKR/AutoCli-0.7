# Models import:
from network.datasets.models.nhrp_data import NhrpData

# Serializer import:
from ..serializers.nhrp_data import NhrpDataSerializer

# Paginator import:
from network.all.base_api.base_pagination import BaseSmallPaginator

# Base mode view set import:
from network.all.base_api.base_modelviewset import BaseRoModelViewSet

# Filter import:
from network.datasets.filters.nhrp_data import NhrpDataFilter


# ViewSet model classes:
class NhrpDataView(BaseRoModelViewSet):
    """
    A ViewSet for viewing and editing object/s.
    """
    # Basic API view parameters:
    queryset = NhrpData.objects.all()
    pagination_class = BaseSmallPaginator
    # Serializer classes:
    serializer_class = NhrpDataSerializer
    # Django rest framework filters:
    filterset_class = NhrpDataFilter
    ordering_fields = BaseRoModelViewSet.base_ordering_fields + [
        'update',
    ]
