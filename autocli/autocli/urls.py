# Django import:
from django.contrib import admin
from django.urls import path, include

# URLs registration:
urlpatterns = [
    # Django admin registration:
    path('admin/', admin.site.urls),


    # Inventory/device registration:
    path('inventory/test/', include('inventory.devices.urls')),
    path('api/inventory/', include('inventory.devices.api.urls')),

    # Rest framework registration:
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
