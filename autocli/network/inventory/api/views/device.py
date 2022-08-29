# Paginator import:
from network.all.base_api.base_pagination import BaseSmallPaginator

# Model import:
from network.inventory.models.device import Device

# Serializer import:
from ..serializers.device import DeviceSerializer
from ..serializers.simple_device import SimpleDeviceSerializer

# Base mode view set import:
from network.all.base_api.base_modelviewset import BaseModelViewSet

# Filter set class import:
from network.inventory.filters.device import DeviceFilter


# ViewSet model classes:
class DeviceView(BaseModelViewSet):
    """
    A ViewSet for viewing and editing object/s.
    """
    # Basic API view parameters:
    queryset = Device.objects.all()
    pagination_class = BaseSmallPaginator
    # Serializer classes:
    serializer_class = DeviceSerializer
    single_serializer_class = SimpleDeviceSerializer
    # Django rest framework filters:
    filterset_class = DeviceFilter
    search_fields = BaseModelViewSet.base_search_fields + [
        'name',
        'description',
        'hostname',
    ]
    ordering_fields = BaseModelViewSet.base_ordering_fields + [
        'name',
        'hostname',
    ]


class SimpleDeviceView(BaseModelViewSet):
    """
    A simple ViewSet for viewing and editing object/s.
    """
    # Execute API view from Swagger schema:
    exclude_from_schema = True
    swagger_schema = None
    # Basic API view parameters:
    queryset = Device.objects.all()
    pagination_class = BaseSmallPaginator
    # Serializer classes:
    serializer_class = SimpleDeviceSerializer
    # Django rest framework filters:
    filterset_class = DeviceFilter
    search_fields = BaseModelViewSet.base_search_fields + [
        'name',
        'description',
        'hostname',
    ]
    ordering_fields = BaseModelViewSet.base_ordering_fields + [
        'name',
        'hostname',
    ]
