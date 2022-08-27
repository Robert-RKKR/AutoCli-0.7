# Django rest framework filters import:
from django_filters.rest_framework import DjangoFilterBackend

# Paginator import:
from network.all.base_api.base_pagination import BaseSmallPaginator

# Model import:
from network.inventory.models.device import Device

# Serializer import:
from ..serializers.device import DeviceSerializer
from ..serializers.simple_device import SimpleDeviceSerializer

# Base mode view set import:
from network.all.base_api.base_modelviewset import BaseModelViewSet


# ViewSet model classes:
class DeviceView(BaseModelViewSet):
    """
    A ViewSet for viewing and editing accounts.
    """
    queryset = Device.objects.all()
    pagination_class = BaseSmallPaginator
    # Serializer classes:
    serializer_class = DeviceSerializer
    single_serializer_class = SimpleDeviceSerializer
    # Django rest framework filters:
    filterset_fields = BaseModelViewSet.base_filterset_fields + [
        'name'
    ]
    search_fields = BaseModelViewSet.base_search_fields + [
        'name',
        'description',
        'hostname'
    ]
    ordering_fields = BaseModelViewSet.base_ordering_fields + [
        'name',
        'hostname'
    ]


class SimpleDeviceView(BaseModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = Device.objects.all()
    serializer_class = SimpleDeviceSerializer
    pagination_class = BaseSmallPaginator
    # Django rest framework filters:
