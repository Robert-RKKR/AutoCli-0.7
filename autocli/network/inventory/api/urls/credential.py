# Rest framework import:
from rest_framework import routers

# Standard view import:
from network.inventory.api.views.credential import CredentialView

# Simple view import:
from network.inventory.api.views.credential import SimpleCredentialView

# Register router:
router = routers.DefaultRouter()

# App name registration:
app_name = 'api-inventory'

# Standard view route registration:
router.register(r'credential', CredentialView, basename='credential')

# Simple view route registration:
router.register(r'simple_credential', SimpleCredentialView, basename='simple_credential')

# Add urlpatterns:
urlpatterns = router.urls
