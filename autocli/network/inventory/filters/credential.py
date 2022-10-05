# Base filter import:
from network.all.base_model.filters.base_filter import BaseFilter

# Model import:
from network.inventory.models.credential import Credential


# Filters:
class CredentialFilter(BaseFilter):

    class Meta:

        model = Credential
        fields = {
            'id': ['exact', 'icontains'],
            'active': ['exact'],
            'name': ['exact', 'icontains'],
            'description': ['exact', 'icontains'],
            'username': ['exact', 'icontains'],
        }
