# Root view import:
from network.inventory.api.views.root import InventoryRootView

# Standard view import:
from network.inventory.api.views.device_type_template import DeviceTypeTemplateView
from network.inventory.api.views.device_type import DeviceTypeView
from network.inventory.api.views.credential import CredentialView
from network.inventory.api.views.device import DeviceView
from network.inventory.api.views.group import GroupView
from network.inventory.api.views.root import InventoryRootView

# Simple view import:
from network.inventory.api.views.device_type_template import SimpleDeviceTypeTemplateView
from network.inventory.api.views.device_type import SimpleDeviceTypeView
from network.inventory.api.views.credential import SimpleCredentialView
from network.inventory.api.views.device import SimpleDeviceView
from network.inventory.api.views.group import SimpleGroupView

# Base default route import:
from network.all.base_api.base_default_router import BaseDefaultRouter

# Register router:
router = BaseDefaultRouter()

# App name registration:
app_name = 'api-inventory'

# Root api view route registration:
router.APIRootView = InventoryRootView

# Standard view route registration:
router.register(r'device_type_template', DeviceTypeTemplateView, basename='device_type_template')
router.register(r'device_type', DeviceTypeView, basename='device_type')
router.register(r'credential', CredentialView, basename='credential')
router.register(r'device', DeviceView, basename='device')
router.register(r'group', GroupView, basename='group')

# Simple view route registration:
router.register(r'simple_device_type_template', SimpleDeviceTypeTemplateView, basename='simple_device_type_template')
router.register(r'simple_device_type', SimpleDeviceTypeView, basename='simple_device_type')
router.register(r'simple_credential', SimpleCredentialView, basename='simple_credential')
router.register(r'simple_device', SimpleDeviceView, basename='simple_device')
router.register(r'simple_group', SimpleGroupView, basename='simple_group')

# Add urlpatterns:
urlpatterns = router.urls
