# Models import:
from network.datasets.models.environment_data import EnvironmentData

# Serializer import:
from ..serializers.environment_data import EnvironmentDataSerializer

# Paginator import:
from network.all.base_api.base_pagination import BaseSmallPaginator

# Base mode view set import:
from network.all.base_api.base_modelviewset import BaseRoModelViewSet

# Filter import:
from network.datasets.filters.environment_data import EnvironmentDataFilter


# ViewSet model classes:
class EnvironmentDataView(BaseRoModelViewSet):
    """
    A ViewSet for viewing and editing object/s.
    """
    # Basic API view parameters:
    queryset = EnvironmentData.objects.all()
    pagination_class = BaseSmallPaginator
    # Serializer classes:
    serializer_class = EnvironmentDataSerializer
    # Django rest framework filters:
    filterset_class = EnvironmentDataFilter
    ordering_fields = BaseRoModelViewSet.base_ordering_fields + [
        'update',
    ]
