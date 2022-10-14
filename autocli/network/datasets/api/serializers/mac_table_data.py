# Rest framework import:
from rest_framework.serializers import HyperlinkedIdentityField

# Base serializer import:
from network.all.base_api.base_serializer import BaseSerializer

# Models import:
from network.datasets.models.mac_table_data import MacTableData

# Other serializer import:
from network.updates.api.serializers.update import UpdateSerializer


# Serializer class:
class MacTableDataSerializer(BaseSerializer):

    # Object URL definition:
    url = HyperlinkedIdentityField(
        view_name='api-datasets:mac_table_data-detail',
        read_only=False,
    )
    # Object relation definition:
    update = UpdateSerializer(
        many=False,
        read_only=True,
    )

    class Meta:

        model = MacTableData
        fields = BaseSerializer.base_fields + [
            'update',
            'vlan',
            'mac',
            'type',
            'age',
            'secure',
            'ntfy',
            'ports',
            'ports_list',
        ]
