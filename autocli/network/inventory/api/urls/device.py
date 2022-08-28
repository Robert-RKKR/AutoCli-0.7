# Rest framework import:
from rest_framework import routers

# Standard view import:
from network.inventory.api.views.device import DeviceView

# Simple view import:
from network.inventory.api.views.device import SimpleDeviceView

# Register router:
router = routers.DefaultRouter()

# App name registration:
app_name = 'api-inventory'

# Standard view route registration:
router.register(r'device', DeviceView, basename='device')

# Simple view route registration:
router.register(r'simple_device', SimpleDeviceView, basename='simple_device')

# Add urlpatterns:
urlpatterns = router.urls
