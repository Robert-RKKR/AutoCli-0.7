# Rest framework import:
from rest_framework.authentication import SessionAuthentication
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import DjangoModelPermissions

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
    serializer_class = DeviceTypeTemplateSerializer
    single_serializer_class = SimpleDeviceTypeTemplateSerializer
    # Authentication and permissions:
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [DjangoModelPermissions]


class SimpleDeviceTypeTemplateView(BaseModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = DeviceTypeTemplate.objects.all()
    serializer_class = DeviceTypeTemplateSerializer
    pagination_class = BaseSmallPaginator
    # Authentication and permissions:
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [DjangoModelPermissions]
