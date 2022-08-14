# Django Import:
from django.urls import path

# Application Import:
from .consumers import NotificationConsumer

ws_urlpatterns = [
    path('ws/notifications/', NotificationConsumer.as_asgi()),
]