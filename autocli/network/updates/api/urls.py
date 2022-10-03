# Django Import:
from django.urls import path

# Root view import:
from network.updates.api.views.root import UpdatesRootView

# View import:
from .views.collected_data import CollectedDataRetrieveAPI
from .views.collected_data import CollectedDataListAPI
from .views.snapshot import SnapshotRetrieveAPI
from .views.snapshot import SnapshotListAPI
from .views.update import UpdateRetrieveAPI
from .views.update import UpdateListAPI

# Base default route import:
from network.all.base_api.base_default_router import BaseDefaultRouter

# Register router:
router = BaseDefaultRouter()

# App name registration:
app_name = 'api-updates'

# Root api view route registration:
router.APIRootView = UpdatesRootView

urlpatterns = [
    path('collected_data/<int:pk>', CollectedDataRetrieveAPI.as_view(), name='collected_data'),
    path('collected_dates/', CollectedDataListAPI.as_view(), name='collected_dates'),
    path('snapshot/<int:pk>', SnapshotRetrieveAPI.as_view(), name='snapshot'),
    path('snapshots/', SnapshotListAPI.as_view(), name='snapshots'),
    path('update/<int:pk>', UpdateRetrieveAPI.as_view(), name='update'),
    path('updates/', UpdateListAPI.as_view(), name='updates'),
]

# Add urlpatterns:
urlpatterns += router.urls
