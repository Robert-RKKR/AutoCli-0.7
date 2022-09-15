# Rest Django import:
from rest_framework import generics

# Models import:
from network.updates.models.snapshot import Snapshot

# Serializer import:
from ..serializers.snapshot import SnapshotSerializer

# Paginator import:
from network.all.base_api.base_pagination import BaseSmallPaginator


# All Change Log views:
class SnapshotListAPI(generics.ListAPIView):
    queryset = Snapshot.objects.all()
    serializer_class = SnapshotSerializer
    pagination_class = BaseSmallPaginator


class SnapshotRetrieveAPI(generics.RetrieveAPIView):
    queryset = Snapshot.objects.all()
    serializer_class = SnapshotSerializer
