# Rest framework import:
from rest_framework import routers

# Standard view import:
from network.inventory.api.views.device_type import DeviceTypeView

# Simple view import:
from network.inventory.api.views.device_type import SimpleDeviceTypeView
# Register router:
router = routers.DefaultRouter()

# App name registration:
app_name = 'api-inventory'

# Standard view route registration:
router.register(r'device_type', DeviceTypeView, basename='device_type')

# Simple view route registration:
router.register(r'simple_device_type', SimpleDeviceTypeView, basename='simple_device_type')

# Add urlpatterns:
urlpatterns = router.urls
