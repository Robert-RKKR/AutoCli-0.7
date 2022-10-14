# Root view import:
from network.datasets.api.views.root import DatasetsRootView

# View import:
from .views.access_list_data import AccessListDataView
from .views.arp_table_data import ArpTableDataView
from .views.device_data import DeviceDataView
from .views.dmvpn_data import DmvpnDataView
from .views.environment_data import EnvironmentDataDataView
from .views.etherchannel_data import EtherchannelDataView
from .views.interface_data import InterfaceDataView
from .views.mac_table_data import MacTableDataView
from .views.module_data import ModuleDataView
from .views.neighbor_data import NeighborDataView
from .views.nhrp_data import NhrpDataView
from .views.router_data import RouterDataView

# Base default route import:
from network.all.base_api.base_default_router import BaseDefaultRouter

# Register router:
router = BaseDefaultRouter()

# App name registration:
app_name = 'api-datasets'

# Root api view route registration:
router.APIRootView = DatasetsRootView

# Standard view route registration:
router.register(r'access_list_data', AccessListDataView, basename='access_list_data')
router.register(r'arp_table_data', ArpTableDataView, basename='arp_table_data')
router.register(r'device_data', DeviceDataView, basename='device_data')
router.register(r'dmvpn_data', DmvpnDataView, basename='dmvpn_data')
router.register(r'environment_data', EnvironmentDataDataView, basename='environment_data')
router.register(r'etherchannel_data', EtherchannelDataView, basename='etherchannel_data')
router.register(r'interface_data', InterfaceDataView, basename='interface_data')
router.register(r'mac_table_data', MacTableDataView, basename='mac_table_data')
router.register(r'module_data', ModuleDataView, basename='module_data')
router.register(r'neighbor_data', NeighborDataView, basename='neighbor_data')
router.register(r'nhrp_data', NhrpDataView, basename='nhrp_data')
router.register(r'router_data', RouterDataView, basename='router_data')

# Add urlpatterns:
urlpatterns = router.urls
