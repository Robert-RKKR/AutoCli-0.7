# Django Import:
from django.urls import path

# Application Import:
from inventory.devices.views.test import test

app_name = 'inventory.devices.'

urlpatterns = [
    path('test', test, name='test'),
]
