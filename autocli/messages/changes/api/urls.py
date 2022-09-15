# Django Import:
from django.urls import path

# View import:
from .views.change_log import ChangeLogRetrieveAPI
from .views.change_log import ChangeLogListAPI

# App name registration:
app_name = 'api-changes'

urlpatterns = [
    path('change_log/<int:pk>', ChangeLogRetrieveAPI.as_view(), name='change_log'),
    path('change_logs/', ChangeLogListAPI.as_view(), name='change_logs'),
]
