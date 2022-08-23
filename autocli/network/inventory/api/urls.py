# Rest framework import:
from rest_framework import routers

# Views import:
from network.inventory.api.views.device_type import DeviceTypeView
from network.inventory.api.views.credential import CredentialView
from network.inventory.api.views.device import DeviceView
from network.inventory.api.views.group import GroupView


from network.inventory.api.views.device import SimpleDeviceView

# Register router:
router = routers.DefaultRouter()

# App name registration:
app_name = 'api-inventory'

# URLs registration:
router.register(r'device_type', DeviceTypeView, basename='device_type')
router.register(r'credential', CredentialView, basename='credential')
router.register(r'device', DeviceView, basename='device')
router.register(r'group', GroupView, basename='group')


router.register(r'device_simple', SimpleDeviceView, basename='device_simple')

# Add urlpatterns:
urlpatterns = router.urls
