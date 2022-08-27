# Rest framework import:
from rest_framework.authentication import SessionAuthentication
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import DjangoModelPermissions

# Paginator import:
from network.all.base_api.base_pagination import BaseSmallPaginator

# Paginator import:
from network.all.base_api.base_pagination import BaseSmallPaginator

# Model import:
from network.inventory.models.group import Group

# Serializer import:
from ..serializers.simple_group import SimpleGroupSerializer
from ..serializers.group import GroupSerializer

# Base mode view set import:
from network.all.base_api.base_modelviewset import BaseModelViewSet


# ViewSet model classes:
class GroupView(BaseModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = Group.objects.all()
    pagination_class = BaseSmallPaginator
    # Serializer classes:
    serializer_class = GroupSerializer
    single_serializer_class = SimpleGroupSerializer
    # Authentication and permissions:
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [DjangoModelPermissions]


class SimpleGroupView(BaseModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = Group.objects.all()
    serializer_class = SimpleGroupSerializer
    pagination_class = BaseSmallPaginator
    # Authentication and permissions:
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [DjangoModelPermissions]
