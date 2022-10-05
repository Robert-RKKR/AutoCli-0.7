# Rest Django import:
from rest_framework import generics

# Models import:
from messages.logger.models.log import Log

# Serializer import:
from messages.logger.api.serializers.log import LogSerializer

# Paginator import:
from messages.all.base_api.base_pagination import BaseLargePaginator

# Base mode view set import:
from messages.all.base_api.base_modelviewset import BaseRoModelViewSet

# Filter import:
from messages.logger.filters.log import LogFilter


# ViewSet model classes:
class LogView(BaseRoModelViewSet):
    """
    A ViewSet for viewing and editing object/s.
    """
    # Basic API view parameters:
    queryset = Log.objects.all()
    pagination_class = BaseLargePaginator
    # Serializer classes:
    serializer_class = LogSerializer
    # Django rest framework filters:
    filterset_class = LogFilter
    search_fields = BaseRoModelViewSet.base_search_fields + [
        'message'
    ]
    ordering_fields = BaseRoModelViewSet.base_ordering_fields + [
        'app_name',
        'model_name',
        'application',
        'severity',
    ]
