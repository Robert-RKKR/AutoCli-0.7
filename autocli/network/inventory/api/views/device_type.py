# Paginator import:
from network.all.base_api.base_pagination import BaseSmallPaginator

# Model import:
from network.inventory.models.device_type import DeviceType

# Serializer import:
from ..serializers.simple_device_type import SimpleDeviceTypeSerializer
from ..serializers.device_type import DeviceTypeSerializer

# Base mode view set import:
from network.all.base_api.base_modelviewset import BaseModelViewSet


# ViewSet model classes:
class DeviceTypeView(BaseModelViewSet):
    """
    A ViewSet for viewing and editing object/s.
    """
    queryset = DeviceType.objects.all()
    pagination_class = BaseSmallPaginator
    # Serializer classes:
    serializer_class = DeviceTypeSerializer
    single_serializer_class = SimpleDeviceTypeSerializer
    # Django rest framework filters:


class SimpleDeviceTypeView(BaseModelViewSet):
    """
    A simple ViewSet for viewing and editing object/s.
    """
    queryset = DeviceType.objects.all()
    serializer_class = SimpleDeviceTypeSerializer
    pagination_class = BaseSmallPaginator
    # Django rest framework filters:
