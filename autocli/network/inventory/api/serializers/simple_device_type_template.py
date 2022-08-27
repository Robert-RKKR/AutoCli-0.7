# Rest framework import:
from rest_framework import serializers

# Base serializer import:
from network.all.base_api.base_serializer import BaseSerializer

# Model import:
from network.inventory.models.device_type import DeviceType

# Model import:
from network.inventory.models.device_type_template import DeviceTypeTemplate


# Serializer class:
class SimpleDeviceTypeTemplateSerializer(BaseSerializer):

    # Object URL definition:
    url = serializers.HyperlinkedIdentityField(
        view_name='api-inventory:device_type_template-detail',
        read_only=False,
    )
    # Object relation definition:
    device_type = serializers.PrimaryKeyRelatedField(
        queryset=DeviceType.objects.all()
    )

    class Meta:

        model = DeviceTypeTemplate
        fields = BaseSerializer.base_fields + [
            'special',
            'vrf',
            'device_type',
            'command',
            'sfm_expression',
        ]
        read_only_fields = BaseSerializer.base_read_only_fields
