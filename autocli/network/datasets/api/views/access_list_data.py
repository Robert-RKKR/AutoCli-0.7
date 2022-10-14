# Models import:
from network.datasets.models.access_list_data import AccessListData

# Serializer import:
from ..serializers.access_list_data import AccessListDataSerializer

# Paginator import:
from network.all.base_api.base_pagination import BaseSmallPaginator

# Base mode view set import:
from network.all.base_api.base_modelviewset import BaseRoModelViewSet

# Filter import:
from network.datasets.filters.access_list_data import AccessListDataFilter


# ViewSet model classes:
class AccessListDataView(BaseRoModelViewSet):
    """
    A ViewSet for viewing and editing object/s.
    """
    # Basic API view parameters:
    queryset = AccessListData.objects.all()
    pagination_class = BaseSmallPaginator
    # Serializer classes:
    serializer_class = AccessListDataSerializer
    # Django rest framework filters:
    filterset_class = AccessListDataFilter
    search_fields = BaseRoModelViewSet.base_search_fields + [
        'XXX',
    ]
    ordering_fields = BaseRoModelViewSet.base_ordering_fields + [
        'update',
        'XXX',
    ]
