# Rest framework import:
from rest_framework import routers

# Standard view import:
from network.inventory.api.views.group import GroupView

# Simple view import:
from network.inventory.api.views.group import SimpleGroupView

# Register router:
router = routers.DefaultRouter()

# App name registration:
app_name = 'api-inventory'

# Standard view route registration:
router.register(r'group', GroupView, basename='group')

# Simple view route registration:
router.register(r'simple_group', SimpleGroupView, basename='simple_group')

# Add urlpatterns:
urlpatterns = router.urls
