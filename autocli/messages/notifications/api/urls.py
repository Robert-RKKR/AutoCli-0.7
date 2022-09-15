# Django Import:
from django.urls import path

# View import:
from .views.notification import NotificationListAPI
from .views.notification import NotificationRetrieveAPI

# App name registration:
app_name = 'api-notifications'

urlpatterns = [
    path('notification/<int:pk>', NotificationRetrieveAPI.as_view(), name='notification'),
    path('notifications/', NotificationListAPI.as_view(), name='notifications'),
]
