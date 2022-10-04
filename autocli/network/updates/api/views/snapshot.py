# Models import:
from network.updates.models.snapshot import Snapshot

# Serializer import:
from ..serializers.snapshot import SnapshotSerializer

# Paginator import:
from network.all.base_api.base_pagination import BaseSmallPaginator

# Base mode view set import:
from network.all.base_api.base_modelviewset import BaseRoModelViewSet


# ViewSet model classes:
class SnapshotView(BaseRoModelViewSet):
    """
    A ViewSet for viewing and editing object/s.
    """
    # Basic API view parameters:
    queryset = Snapshot.objects.all()
    pagination_class = BaseSmallPaginator
    # Serializer classes:
    serializer_class = SnapshotSerializer
    # Django rest framework filters:
    # filterset_class = CredentialFilter
    # search_fields = BaseRoModelViewSet.base_search_fields + [
    #     'name'
    # ]
    # ordering_fields = BaseRoModelViewSet.base_ordering_fields + [
    #     'name'
    # ]
