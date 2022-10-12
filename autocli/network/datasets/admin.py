from django.contrib import admin

# Models import:
from network.datasets.models.access_list_data import AccessListData
from network.datasets.models.arp_table_data import ArpTableData
from network.datasets.models.device_data import DeviceData
from network.datasets.models.dmvpn_data import DmvpnData
from network.datasets.models.environment_data import EnvironmentData
from network.datasets.models.etherchannel_data import EtherchannelData
from network.datasets.models.interface_data import InterfaceData
from network.datasets.models.mac_table_data import MacTableData
from network.datasets.models.module_data import ModuleData
from network.datasets.models.neighbor_data import NeighborData
from network.datasets.models.nhrp_data import NhrpData
from network.datasets.models.router_data import RouterData

# Register your models here.
admin.site.register(AccessListData)
admin.site.register(ArpTableData)
admin.site.register(DeviceData)
admin.site.register(DmvpnData)
admin.site.register(EnvironmentData)
admin.site.register(EtherchannelData)
admin.site.register(InterfaceData)
admin.site.register(MacTableData)
admin.site.register(ModuleData)
admin.site.register(NeighborData)
admin.site.register(NhrpData)
admin.site.register(RouterData)
