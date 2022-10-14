# Paginator import:
from network.all.base_api.base_pagination import BaseSmallPaginator

# Model import:
from network.inventory.models.device_type_template import DeviceTypeTemplate

# Serializer import:
from ..serializers.simple_device_type_template import SimpleDeviceTypeTemplateSerializer
from ..serializers.device_type_template import DeviceTypeTemplateSerializer

# Base mode view set import:
from network.all.base_api.base_modelviewset import BaseModelViewSet

# Filter set class import:
from network.inventory.filters.device_type_template import DeviceTypeTemplateFilter


# ViewSet model classes:
class DeviceTypeTemplateView(BaseModelViewSet):
    """
    A ViewSet for viewing and editing object/s.
    """
    # Basic API view parameters:
    queryset = DeviceTypeTemplate.objects.all()
    pagination_class = BaseSmallPaginator
    # Serializer classes:
    serializer_class = DeviceTypeTemplateSerializer
    single_serializer_class = SimpleDeviceTypeTemplateSerializer
    # Django rest framework filters:
    filterset_class = DeviceTypeTemplateFilter
    search_fields = BaseModelViewSet.base_search_fields + [
        'command',
        'sfm_expression',
    ]
    ordering_fields = BaseModelViewSet.base_ordering_fields + [
        'vrf',
        'special',
    ]


class SimpleDeviceTypeTemplateView(BaseModelViewSet):
    """
    A simple ViewSet for viewing and editing object/s.
    """
    # Execute API view from Swagger schema:
    exclude_from_schema = True
    swagger_schema = None
    # Basic API view parameters:
    queryset = DeviceTypeTemplate.objects.all()
    pagination_class = BaseSmallPaginator
    # Serializer classes:
    serializer_class = DeviceTypeTemplateSerializer
    # Django rest framework filters:
    filterset_class = DeviceTypeTemplateFilter
    search_fields = BaseModelViewSet.base_search_fields + [
        'command',
        'sfm_expression',
        'device_data_corelation',
    ]
    ordering_fields = BaseModelViewSet.base_ordering_fields + [
        'vrf',
        'special',
        'device_data_corelation',
    ]
