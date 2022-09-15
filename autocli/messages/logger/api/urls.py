# Django Import:
from django.urls import path

# View import:
from .views.log import LogRetrieveAPI
from .views.log import LogListAPI

# App name registration:
app_name = 'api-logger'

urlpatterns = [
    path('log/<int:pk>', LogRetrieveAPI.as_view(), name='log'),
    path('logs/', LogListAPI.as_view(), name='logs'),
]
