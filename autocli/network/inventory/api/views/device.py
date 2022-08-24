# Rest framework import:
from rest_framework import viewsets

# Paginator import:
from network.all.base_api.base_pagination import BaseSmallPaginator

# Model import:
from network.inventory.models.device import Device

# Serializer import:
from ..serializers.device import DeviceSerializer
from ..serializers.simple_device import SimpleDeviceSerializer


from network.all.base_api.base_modelviewset import BaseModelViewSet

class DeviceView(BaseModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
    pagination_class = BaseSmallPaginator
    create_serializer_class = SimpleDeviceSerializer


class SimpleDeviceView(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = Device.objects.all()
    serializer_class = SimpleDeviceSerializer
    pagination_class = BaseSmallPaginator
