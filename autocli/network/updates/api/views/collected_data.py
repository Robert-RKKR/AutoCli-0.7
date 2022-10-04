# Models import:
from network.updates.models.collected_data import CollectedData

# Serializer import:
from ..serializers.collected_data import CollectedDataSerializer

# Paginator import:
from network.all.base_api.base_pagination import BaseSmallPaginator

# Base mode view set import:
from network.all.base_api.base_modelviewset import BaseRoModelViewSet


# ViewSet model classes:
class CollectedDataView(BaseRoModelViewSet):
    """
    A ViewSet for viewing and editing object/s.
    """
    # Basic API view parameters:
    queryset = CollectedData.objects.all()
    pagination_class = BaseSmallPaginator
    # Serializer classes:
    serializer_class = CollectedDataSerializer
    # Django rest framework filters:
    # filterset_class = CredentialFilter
    search_fields = BaseRoModelViewSet.base_search_fields + [
        'command_name',
        'command_raw_data',
        'command_processed_data',
    ]
    ordering_fields = BaseRoModelViewSet.base_ordering_fields + [
        'update',
        'result_status',
        'raw_data_status',
        'processed_data_status',
    ]
