# Django import:
from django.contrib import admin
from django.urls import path, include

# URLs registration:
urlpatterns = [
    # Django admin registration:
    path('admin/', admin.site.urls),


    # Inventory/device registration:
    path('network/test/', include('network.inventory.urls')),
    path('api/inventory/', include('network.inventory.api.urls')),

    # Rest framework registration:
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
