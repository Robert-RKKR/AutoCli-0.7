# Root view import:
from network.updates.api.views.root import UpdatesRootView

# View import:
from .views.collected_data import CollectedDataView
from .views.snapshot import SnapshotView
from .views.update import UpdateView

# Base default route import:
from network.all.base_api.base_default_router import BaseDefaultRouter

# Register router:
router = BaseDefaultRouter()

# App name registration:
app_name = 'api-updates'

# Root api view route registration:
router.APIRootView = UpdatesRootView

# Standard view route registration:
router.register(r'collected_data', CollectedDataView, basename='collected_data')
router.register(r'snapshot', SnapshotView, basename='snapshot')
router.register(r'update', UpdateView, basename='update')

# Add urlpatterns:
urlpatterns = router.urls
