# Paginator import:
from network.all.base_api.base_pagination import BaseSmallPaginator

# Model import:
from network.inventory.models.device_type import DeviceType

# Serializer import:
from ..serializers.simple_device_type import SimpleDeviceTypeSerializer
from ..serializers.device_type import DeviceTypeSerializer

# Base mode view set import:
from network.all.base_api.base_modelviewset import BaseModelViewSet

# Filter set class import:
from network.inventory.filters.device_type import DeviceTypeFilter


# ViewSet model classes:
class DeviceTypeView(BaseModelViewSet):
    """
    A ViewSet for viewing and editing object/s.
    """
    # Basic API view parameters:
    queryset = DeviceType.objects.all()
    pagination_class = BaseSmallPaginator
    # Serializer classes:
    serializer_class = DeviceTypeSerializer
    single_serializer_class = SimpleDeviceTypeSerializer
    # Django rest framework filters:
    filterset_class = DeviceTypeFilter
    search_fields = BaseModelViewSet.base_search_fields + [
        'name',
        'description',
        'netmiko_name',
    ]
    ordering_fields = BaseModelViewSet.base_ordering_fields + [
        'name',
        'netmiko_name',
    ]


class SimpleDeviceTypeView(BaseModelViewSet):
    """
    A simple ViewSet for viewing and editing object/s.
    """
    # Execute API view from Swagger schema:
    exclude_from_schema = True
    swagger_schema = None
    # Basic API view parameters:
    queryset = DeviceType.objects.all()
    pagination_class = BaseSmallPaginator
    # Serializer classes:
    serializer_class = SimpleDeviceTypeSerializer
    # Django rest framework filters:
    filterset_class = DeviceTypeFilter
    search_fields = BaseModelViewSet.base_search_fields + [
        'name',
        'description',
        'netmiko_name',
    ]
    ordering_fields = BaseModelViewSet.base_ordering_fields + [
        'name',
        'netmiko_name',
    ]
