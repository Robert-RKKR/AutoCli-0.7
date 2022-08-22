# Django Import:
from django.urls import path

# Application Import:
from inventory.devices.views.test import test

# App name registration:
app_name = 'inventory.devices.'

# URLs registration:
urlpatterns = [
    path('test', test, name='test'),
]
