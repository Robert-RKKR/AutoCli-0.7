# Models import:
from messages.changes.models.change_log import ChangeLog

# Serializer import:
from messages.changes.api.serializers.change_log import ChangeLogSerializer

# Paginator import:
from messages.all.base_api.base_pagination import BaseMediumPaginator

# Base mode view set import:
from messages.all.base_api.base_modelviewset import BaseRoModelViewSet

# Filter import:
from messages.changes.filters.change_log import ChangeLogFilter


# ViewSet model classes:
class ChangeLogView(BaseRoModelViewSet):
    """
    A ViewSet for viewing and editing object/s.
    """
    # Basic API view parameters:
    queryset = ChangeLog.objects.all()
    pagination_class = BaseMediumPaginator
    # Serializer classes:
    serializer_class = ChangeLogSerializer
    # Django rest framework filters:
    filterset_class = ChangeLogFilter
    search_fields = BaseRoModelViewSet.base_search_fields + [
        'after',
        'object_representation'
    ]
    ordering_fields = BaseRoModelViewSet.base_ordering_fields + [
        'app_name',
        'model_name',
        'action'
    ]
