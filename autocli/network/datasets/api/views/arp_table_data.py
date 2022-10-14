# Models import:
from network.datasets.models.arp_table_data import ArpTableData

# Serializer import:
from ..serializers.arp_table_data import ArpTableDataSerializer

# Paginator import:
from network.all.base_api.base_pagination import BaseSmallPaginator

# Base mode view set import:
from network.all.base_api.base_modelviewset import BaseRoModelViewSet

# Filter import:
from network.datasets.filters.arp_table_data import ArpTableDataFilter


# ViewSet model classes:
class ArpTableDataView(BaseRoModelViewSet):
    """
    A ViewSet for viewing and editing object/s.
    """
    # Basic API view parameters:
    queryset = ArpTableData.objects.all()
    pagination_class = BaseSmallPaginator
    # Serializer classes:
    serializer_class = ArpTableDataSerializer
    # Django rest framework filters:
    filterset_class = ArpTableDataFilter
    ordering_fields = BaseRoModelViewSet.base_ordering_fields + [
        'update',
    ]
