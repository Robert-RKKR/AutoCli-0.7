# Rest framework import:
from rest_framework import routers

# Standard view import:
from network.inventory.api.views.device_type_template import DeviceTypeTemplateView

# Simple view import:
from network.inventory.api.views.device_type_template import SimpleDeviceTypeTemplateView

# Register router:
router = routers.DefaultRouter()

# App name registration:
app_name = 'api-inventory'

# Standard view route registration:
router.register(r'device_type_template', DeviceTypeTemplateView, basename='device_type_template')

# Simple view route registration:
router.register(r'simple_device_type_template', SimpleDeviceTypeTemplateView, basename='simple_device_type_template')

# Add urlpatterns:
urlpatterns = router.urls
