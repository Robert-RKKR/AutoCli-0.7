# Models import:
from network.updates.models.update import Update

# Serializer import:
from ..serializers.update import UpdateSerializer

# Paginator import:
from network.all.base_api.base_pagination import BaseSmallPaginator

# Base mode view set import:
from network.all.base_api.base_modelviewset import BaseRoModelViewSet


# ViewSet model classes:
class UpdateView(BaseRoModelViewSet):
    """
    A ViewSet for viewing and editing object/s.
    """
    # Basic API view parameters:
    queryset = Update.objects.all()
    pagination_class = BaseSmallPaginator
    # Serializer classes:
    serializer_class = UpdateSerializer
    # Django rest framework filters:
    # filterset_class = CredentialFilter
    ordering_fields = BaseRoModelViewSet.base_ordering_fields + [
        'device',
        'snapshot',
        'status',
        'result_status',
    ]
