# Models import:
from network.datasets.models.device_data import DeviceData

# Serializer import:
from ..serializers.device_data import DeviceDataSerializer

# Paginator import:
from network.all.base_api.base_pagination import BaseSmallPaginator

# Base mode view set import:
from network.all.base_api.base_modelviewset import BaseRoModelViewSet

# Filter import:
from network.datasets.filters.device_data import DeviceDataFilter


# ViewSet model classes:
class DeviceDataView(BaseRoModelViewSet):
    """
    A ViewSet for viewing and editing object/s.
    """
    # Basic API view parameters:
    queryset = DeviceData.objects.all()
    pagination_class = BaseSmallPaginator
    # Serializer classes:
    serializer_class = DeviceDataSerializer
    # Django rest framework filters:
    filterset_class = DeviceDataFilter
    search_fields = BaseRoModelViewSet.base_search_fields + [
        'XXX',
    ]
    ordering_fields = BaseRoModelViewSet.base_ordering_fields + [
        'update',
        'XXX',
    ]
