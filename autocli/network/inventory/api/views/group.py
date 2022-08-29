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

# Filter set class import:
from network.inventory.filters.group import GroupFilter


# ViewSet model classes:
class GroupView(BaseModelViewSet):
    """
    A ViewSet for viewing and editing object/s.
    """
    # Basic API view parameters:
    queryset = Group.objects.all()
    pagination_class = BaseSmallPaginator
    # Serializer classes:
    serializer_class = GroupSerializer
    single_serializer_class = SimpleGroupSerializer
    # Django rest framework filters:
    filterset_class = GroupFilter
    search_fields = BaseModelViewSet.base_search_fields + [
        'name',
        'description',
    ]
    ordering_fields = BaseModelViewSet.base_ordering_fields + [
        'name',
        'root_folder',
    ]


class SimpleGroupView(BaseModelViewSet):
    """
    A simple ViewSet for viewing and editing object/s.
    """
    # Execute API view from Swagger schema:
    exclude_from_schema = True
    swagger_schema = None
    # Basic API view parameters:
    queryset = Group.objects.all()
    pagination_class = BaseSmallPaginator
    # Serializer classes:
    serializer_class = SimpleGroupSerializer
    # Django rest framework filters:
    filterset_class = GroupFilter
    search_fields = BaseModelViewSet.base_search_fields + [
        'name',
        'description',
    ]
    ordering_fields = BaseModelViewSet.base_ordering_fields + [
        'name',
        'root_folder',
    ]
