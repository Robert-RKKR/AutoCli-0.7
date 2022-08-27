# Rest framework import:
from rest_framework.authentication import SessionAuthentication
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import DjangoModelPermissions

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
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = Device.objects.all()
    pagination_class = BaseSmallPaginator
    # Serializer classes:
    serializer_class = DeviceSerializer
    single_serializer_class = SimpleDeviceSerializer
    # Authentication and permissions:
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [DjangoModelPermissions]


class SimpleDeviceView(BaseModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = Device.objects.all()
    serializer_class = SimpleDeviceSerializer
    pagination_class = BaseSmallPaginator
    # Authentication and permissions:
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [DjangoModelPermissions]
