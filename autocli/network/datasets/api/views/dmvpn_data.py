# Models import:
from network.datasets.models.dmvpn_data import DmvpnData

# Serializer import:
from ..serializers.dmvpn_data import DmvpnDataSerializer

# Paginator import:
from network.all.base_api.base_pagination import BaseSmallPaginator

# Base mode view set import:
from network.all.base_api.base_modelviewset import BaseRoModelViewSet

# Filter import:
from network.datasets.filters.dmvpn_data import DmvpnDataFilter


# ViewSet model classes:
class DmvpnDataView(BaseRoModelViewSet):
    """
    A ViewSet for viewing and editing object/s.
    """
    # Basic API view parameters:
    queryset = DmvpnData.objects.all()
    pagination_class = BaseSmallPaginator
    # Serializer classes:
    serializer_class = DmvpnDataSerializer
    # Django rest framework filters:
    filterset_class = DmvpnDataFilter
    search_fields = BaseRoModelViewSet.base_search_fields + [
        'XXX',
    ]
    ordering_fields = BaseRoModelViewSet.base_ordering_fields + [
        'update',
        'XXX',
    ]
