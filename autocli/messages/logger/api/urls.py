# Root view import:
from messages.logger.api.views.root import LogRootView

# Django Import:
from django.urls import path

# View import:
from .views.log import LogView

# Base default route import:
from messages.all.base_api.base_default_router import BaseDefaultRouter

# Register router:
router = BaseDefaultRouter()

# App name registration:
app_name = 'api-logger'

# Root api view route registration:
router.APIRootView = LogRootView

# Standard view route registration:
router.register(r'log', LogView, basename='log')

# Add urlpatterns:
urlpatterns = router.urls
