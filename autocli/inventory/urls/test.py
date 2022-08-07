# Django Import:
from django.urls import path

# Application Import:
from inventory.views.test import test

app_name = 'inventory'

urlpatterns = [
    path('test', test, name='test'),
]
