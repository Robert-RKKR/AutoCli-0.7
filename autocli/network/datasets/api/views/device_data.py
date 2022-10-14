# Models import:
from network.datasets.models.XXX import XXX

# Serializer import:
from ..serializers.XXX import XXX

# Paginator import:
from network.all.base_api.base_pagination import BaseSmallPaginator

# Base mode view set import:
from network.all.base_api.base_modelviewset import BaseRoModelViewSet

# Filter import:
from network.datasets.filters.XXX import XXX


# ViewSet model classes:
class DataView(BaseRoModelViewSet):
    """
    A ViewSet for viewing and editing object/s.
    """
    # Basic API view parameters:
    queryset = XXX.objects.all()
    pagination_class = BaseSmallPaginator
    # Serializer classes:
    serializer_class = XXX
    # Django rest framework filters:
    filterset_class = XXX
    search_fields = BaseRoModelViewSet.base_search_fields + [
        'XXX',
    ]
    ordering_fields = BaseRoModelViewSet.base_ordering_fields + [
        'update',
        'XXX',
    ]
