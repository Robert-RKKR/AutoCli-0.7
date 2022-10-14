# Models import:
from network.datasets.models.etherchannel_data import EtherchannelData

# Serializer import:
from ..serializers.etherchannel_data import EtherchannelDataSerializer

# Paginator import:
from network.all.base_api.base_pagination import BaseSmallPaginator

# Base mode view set import:
from network.all.base_api.base_modelviewset import BaseRoModelViewSet

# Filter import:
from network.datasets.filters.etherchannel_data import EtherchannelDataFilter


# ViewSet model classes:
class EtherchannelDataView(BaseRoModelViewSet):
    """
    A ViewSet for viewing and editing object/s.
    """
    # Basic API view parameters:
    queryset = EtherchannelData.objects.all()
    pagination_class = BaseSmallPaginator
    # Serializer classes:
    serializer_class = EtherchannelDataSerializer
    # Django rest framework filters:
    filterset_class = EtherchannelDataFilter
    ordering_fields = BaseRoModelViewSet.base_ordering_fields + [
        'update',
    ]
