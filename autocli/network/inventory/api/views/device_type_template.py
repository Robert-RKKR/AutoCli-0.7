# Rest framework import:
from rest_framework import viewsets

# Paginator import:
from network.all.base_api.base_pagination import BaseSmallPaginator

# Model import:
from network.inventory.models.device_type_template import DeviceTypeTemplate

# Serializer import:
from ..serializers.simple_device_type_template import SimpleDeviceTypeTemplateSerializer
from ..serializers.device_type_template import DeviceTypeTemplateSerializer

# Base mode view set import:
from network.all.base_api.base_modelviewset import BaseModelViewSet


# ViewSet model classes:
class DeviceTypeTemplateView(BaseModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = DeviceTypeTemplate.objects.all()
    pagination_class = BaseSmallPaginator
    # Serializer classes:
    serializer_class = SimpleDeviceTypeTemplateSerializer
    single_serializer_class = DeviceTypeTemplateSerializer


class SimpleDeviceTypeTemplateView(BaseModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = DeviceTypeTemplate.objects.all()
    serializer_class = DeviceTypeTemplateSerializer
    pagination_class = BaseSmallPaginator
