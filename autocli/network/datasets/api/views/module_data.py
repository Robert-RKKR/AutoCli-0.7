# Models import:
from network.datasets.models.module_data import ModuleData

# Serializer import:
from ..serializers.module_data import ModuleDataSerializer

# Paginator import:
from network.all.base_api.base_pagination import BaseSmallPaginator

# Base mode view set import:
from network.all.base_api.base_modelviewset import BaseRoModelViewSet

# Filter import:
from network.datasets.filters.module_data import ModuleDataFilter


# ViewSet model classes:
class ModuleDataView(BaseRoModelViewSet):
    """
    A ViewSet for viewing and editing object/s.
    """
    # Basic API view parameters:
    queryset = ModuleData.objects.all()
    pagination_class = BaseSmallPaginator
    # Serializer classes:
    serializer_class = ModuleDataSerializer
    # Django rest framework filters:
    filterset_class = ModuleDataFilter
    search_fields = BaseRoModelViewSet.base_search_fields + [
        'XXX',
    ]
    ordering_fields = BaseRoModelViewSet.base_ordering_fields + [
        'update',
        'XXX',
    ]
