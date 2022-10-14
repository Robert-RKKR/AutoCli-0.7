# Rest framework import:
from rest_framework.serializers import HyperlinkedIdentityField

# Base serializer import:
from network.all.base_api.base_serializer import BaseSerializer

# Model import:
from network.inventory.models.device_type_template import DeviceTypeTemplate

# Other serializer import:
from .simple_device_type import SimpleDeviceTypeSerializer


# Serializer class:
class DeviceTypeTemplateSerializer(BaseSerializer):

    # Object URL definition:
    url = HyperlinkedIdentityField(
        view_name='api-inventory:device_type_template-detail',
        read_only=False,
    )
    # Object relation definition:
    device_type = SimpleDeviceTypeSerializer(
        many=False,
        read_only=True,
    )

    class Meta:

        model = DeviceTypeTemplate
        fields = BaseSerializer.base_fields + [
            'special',
            'vrf',
            'command',
            'sfm_expression',
            'device_type',
            'device_data_corelation',
        ]
        read_only_fields = BaseSerializer.base_read_only_fields
