# Models import:
from network.datasets.models.mac_table_data import MacTableData

# Serializer import:
from ..serializers.mac_table_data import MacTableDataSerializer

# Paginator import:
from network.all.base_api.base_pagination import BaseSmallPaginator

# Base mode view set import:
from network.all.base_api.base_modelviewset import BaseRoModelViewSet

# Filter import:
from network.datasets.filters.mac_table_data import MacTableDataFilter


# ViewSet model classes:
class MacTableDataView(BaseRoModelViewSet):
    """
    A ViewSet for viewing and editing object/s.
    """
    # Basic API view parameters:
    queryset = MacTableData.objects.all()
    pagination_class = BaseSmallPaginator
    # Serializer classes:
    serializer_class = MacTableDataSerializer
    # Django rest framework filters:
    filterset_class = MacTableDataFilter
    search_fields = BaseRoModelViewSet.base_search_fields + [
        'XXX',
    ]
    ordering_fields = BaseRoModelViewSet.base_ordering_fields + [
        'update',
        'XXX',
    ]
