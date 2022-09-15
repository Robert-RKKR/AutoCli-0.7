# Rest Django import:
from rest_framework import generics

# Models import:
from messages.changes.models.change_log import ChangeLog

# Serializer import:
from messages.changes.api.serializers.change_log import ChangeLogSerializer

# Paginator import:
from messages.all.base_api.base_pagination import BaseMediumPaginator


# All Change Log views:
class ChangeLogListAPI(generics.ListAPIView):
    queryset = ChangeLog.objects.all()
    serializer_class = ChangeLogSerializer
    pagination_class = BaseMediumPaginator


class ChangeLogRetrieveAPI(generics.RetrieveAPIView):
    queryset = ChangeLog.objects.all()
    serializer_class = ChangeLogSerializer
