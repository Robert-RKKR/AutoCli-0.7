# Base filter import:
from network.all.base_model.filters.base_filter import BaseFilter

# Model import:
from network.inventory.models.device_type_template import DeviceTypeTemplate


# Filters:
class DeviceTypeTemplateFilter(BaseFilter):

    class Meta:

        model = DeviceTypeTemplate
        fields = {
            'id': ['exact', 'icontains'],
            'active': ['exact'],
            'special': ['exact'],
            'vrf': ['exact'],
            'command': ['exact', 'icontains'],
            'sfm_expression': ['exact', 'icontains'],
        }
