# Rest framework import:
from rest_framework import routers

# Views import:
from inventory.devices.api.views.credential import CredentialView
from inventory.devices.api.views.device import DeviceView

# Register router:
router = routers.DefaultRouter()

# URLs registration:
router.register(r'credential', CredentialView, basename='credential')
router.register(r'device', DeviceView, basename='device')

# Add urlpatterns:
urlpatterns = router.urls
