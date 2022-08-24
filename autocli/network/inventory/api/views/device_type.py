# Rest framework import:
from rest_framework import viewsets

# Paginator import:
from network.all.base_api.base_pagination import BaseSmallPaginator

# Model import:
from network.inventory.models.device_type import DeviceType

# Serializer import:
from ..serializers.simple_device_type import SimpleDeviceTypeSerializer
from ..serializers.device_type import DeviceTypeSerializer


class DeviceTypeView(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = DeviceType.objects.all()
    serializer_class = DeviceTypeSerializer
    pagination_class = BaseSmallPaginator


class SimpleDeviceTypeView(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = DeviceType.objects.all()
    serializer_class = SimpleDeviceTypeSerializer
    pagination_class = BaseSmallPaginator
