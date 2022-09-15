# Django Import:
from django.urls import path

# View import:
from .views.collected_data import CollectedDataRetrieveAPI
from .views.collected_data import CollectedDataListAPI
from .views.snapshot import SnapshotRetrieveAPI
from .views.snapshot import SnapshotListAPI
from .views.update import UpdateRetrieveAPI
from .views.update import UpdateListAPI

# App name registration:
app_name = 'api-updates'

urlpatterns = [
    path('collected_data/<int:pk>', CollectedDataRetrieveAPI.as_view(), name='collected_data'),
    path('collected_dates/', CollectedDataListAPI.as_view(), name='collected_dates'),
    path('snapshot/<int:pk>', SnapshotRetrieveAPI.as_view(), name='snapshot'),
    path('snapshots/', SnapshotListAPI.as_view(), name='snapshots'),
    path('update/<int:pk>', UpdateRetrieveAPI.as_view(), name='update'),
    path('updates/', UpdateListAPI.as_view(), name='updates'),
]
