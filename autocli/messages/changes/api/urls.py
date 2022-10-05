# Root view import:
from messages.changes.api.views.root import ChangeLogRootView

# View import:
from .views.change_log import ChangeLogView

# Base default route import:
from messages.all.base_api.base_default_router import BaseDefaultRouter

# Register router:
router = BaseDefaultRouter()

# App name registration:
app_name = 'api-changes'

# Root api view route registration:
router.APIRootView = ChangeLogRootView

# Standard view route registration:
router.register(r'change_log', ChangeLogView, basename='change_log')

# Add urlpatterns:
urlpatterns = router.urls
