# Rest Django import:
from rest_framework import generics

# Models import:
from network.updates.models.collected_data import CollectedData

# Serializer import:
from ..serializers.collected_data import CollectedDataSerializer

# Paginator import:
from network.all.base_api.base_pagination import BaseSmallPaginator


# All Change Log views:
class CollectedDataListAPI(generics.ListAPIView):
    queryset = CollectedData.objects.all()
    serializer_class = CollectedDataSerializer
    pagination_class = BaseSmallPaginator


class CollectedDataRetrieveAPI(generics.RetrieveAPIView):
    queryset = CollectedData.objects.all()
    serializer_class = CollectedDataSerializer
