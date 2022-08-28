# Base filter import:
from network.all.base_model.filters.base_filter import BaseFilter

# Model import:
from network.inventory.models.group import Group


# Filters:
class GroupFilter(BaseFilter):

    class Meta:

        model = Group
        fields = {
            'id': ['exact', 'contains'],
            'active': ['exact'],
            'name': ['exact', 'contains'],
            'description': ['exact', 'contains'],
            'root_folder': ['exact'],
            'devices': ['contains'],
            'ssh_port': ['exact', 'contains', 'lt', 'gt'],
            'https_port': ['exact', 'contains', 'lt', 'gt'],
            'credential': ['exact'],
            'certificate': ['exact'],
        }
