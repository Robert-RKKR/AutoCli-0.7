# Rest framework import:
from rest_framework import viewsets

# Model import:
from network.inventory.models.device_type import DeviceType

# Serializer import:
from ..serializers.device_type import DeviceTypeSerializer


class DeviceTypeView(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = DeviceType.objects.all()
    serializer_class = DeviceTypeSerializer
