# Base filter import:
from network.all.base_model.filters.base_filter import BaseFilter

# Model import:
from network.inventory.models.credential import Credential


# Filters:
class CredentialFilter(BaseFilter):

    class Meta:

        model = Credential
        fields = {
            'id': ['exact', 'contains'],
            'active': ['exact'],
            'name': ['exact', 'contains'],
            'description': ['exact', 'contains'],
            'username': ['exact', 'contains'],
        }
