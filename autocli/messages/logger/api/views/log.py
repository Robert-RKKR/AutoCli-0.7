# Rest Django import:
from rest_framework import generics

# Models import:
from messages.logger.models.log import Log

# Serializer import:
from messages.logger.api.serializers.log import LogSerializer

# Paginator import:
from network.all.base_api.base_pagination import BaseLargePaginator


# All Change Log views:
class LogListAPI(generics.ListAPIView):
    queryset = Log.objects.all()
    serializer_class = LogSerializer
    pagination_class = BaseLargePaginator


class LogRetrieveAPI(generics.RetrieveAPIView):
    queryset = Log.objects.all()
    serializer_class = LogSerializer
