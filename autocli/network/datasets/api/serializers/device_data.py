# Rest framework import:
from rest_framework.serializers import HyperlinkedIdentityField

# Base serializer import:
from network.all.base_api.base_serializer import BaseSerializer

# Models import:
from network.datasets.models.device_data import DeviceData

# Other serializer import:
from network.updates.api.serializers.update import UpdateSerializer


# Serializer class:
class DeviceDataSerializer(BaseSerializer):

    # Object URL definition:
    url = HyperlinkedIdentityField(
        view_name='api-datasets:device_data-detail',
        read_only=False,
    )
    # Object relation definition:
    update = UpdateSerializer(
        many=False,
        read_only=True,
    )

    class Meta:

        model = DeviceData
        fields = BaseSerializer.base_fields + [
            'update',
            'version',
            'uptime',
            'hostname',
            'hardware',
            'hardware_list',
            'image',
            'reload_reason',
            'serial',
            'serial_list',
            'license_mode',
            'license_state',
            'max_intf',
            'max_vlans',
            'failover',
            'cluster',
            'uptime_years',
            'uptime_weeks',
            'uptime_days',
            'uptime_hours',
            'uptime_minutes',
            'config_register',
            'mac_list',
            'time',
            'timezone',
            'dayweek',
            'month',
            'day',
            'year',
        ]
