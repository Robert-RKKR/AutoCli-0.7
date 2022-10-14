# Models import:
from network.datasets.models.interface_data import InterfaceData

# Serializer import:
from ..serializers.interface_data import InterfaceDataSerializer

# Paginator import:
from network.all.base_api.base_pagination import BaseSmallPaginator

# Base mode view set import:
from network.all.base_api.base_modelviewset import BaseRoModelViewSet

# Filter import:
from network.datasets.filters.interface_data import InterfaceDataFilter


# ViewSet model classes:
class InterfaceDataView(BaseRoModelViewSet):
    """
    A ViewSet for viewing and editing object/s.
    """
    # Basic API view parameters:
    queryset = InterfaceData.objects.all()
    pagination_class = BaseSmallPaginator
    # Serializer classes:
    serializer_class = InterfaceDataSerializer
    # Django rest framework filters:
    filterset_class = InterfaceDataFilter
    ordering_fields = BaseRoModelViewSet.base_ordering_fields + [
        'update',
    ]
