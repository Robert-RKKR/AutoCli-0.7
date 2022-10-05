# Base filter import:
from network.all.base_model.filters.base_filter import BaseFilter

# Model import:
from network.inventory.models.group import Group


# Filters:
class GroupFilter(BaseFilter):

    class Meta:

        model = Group
        fields = {
            'id': ['exact', 'icontains'],
            'active': ['exact'],
            'name': ['exact', 'icontains'],
            'description': ['exact', 'icontains'],
            'root_folder': ['exact'],
            'devices': ['exact'],
            'ssh_port': ['exact', 'icontains', 'lt', 'gt'],
            'https_port': ['exact', 'icontains', 'lt', 'gt'],
            'credential': ['exact'],
            'certificate': ['exact'],
        }
