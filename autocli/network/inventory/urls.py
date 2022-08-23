# Django Import:
from django.urls import path

# Application Import:
from network.inventory.views.test import test

# App name registration:
app_name = 'inventory'

# URLs registration:
urlpatterns = [
    path('test', test, name='test'),
]
