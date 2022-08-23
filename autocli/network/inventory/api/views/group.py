# Rest framework import:
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework import viewsets

# Paginator import:
from network.all.base_api.base_pagination import BaseSmallPaginator

# Model import:
from network.inventory.models.group import Group

# Serializer import:
from ..serializers.group import GroupSerializer


class GroupView(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    pagination_class = BaseSmallPaginator
