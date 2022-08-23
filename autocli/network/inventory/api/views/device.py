# Rest framework import:
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework import viewsets

# Paginator import:
from network.all.base_api.base_pagination import BaseSmallPaginator

# Model import:
from network.inventory.models.device import Device

# Serializer import:
from ..serializers.device import DeviceSerializer


class DeviceView(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
    pagination_class = BaseSmallPaginator


"""
zmien device na network a network na cos innego.!!!!!!!!!!!!!!!!!
"""