# Rest Django import:
from rest_framework import generics

# Models import:
from network.updates.models.update import Update

# Serializer import:
from ..serializers.update import UpdateSerializer

# Paginator import:
from network.all.base_api.base_pagination import BaseSmallPaginator


# All Change Log views:
class UpdateListAPI(generics.ListAPIView):
    queryset = Update.objects.all()
    serializer_class = UpdateSerializer
    pagination_class = BaseSmallPaginator


class UpdateRetrieveAPI(generics.RetrieveAPIView):
    queryset = Update.objects.all()
    serializer_class = UpdateSerializer
