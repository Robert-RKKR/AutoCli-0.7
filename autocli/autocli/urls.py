# Django import:
from django.contrib import admin
from django.urls import include
from django.urls import re_path
from django.urls import path

# Rest framework import:
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_swagger.views import get_swagger_view

# Register Swagger view:
schema_view = get_swagger_view(title='AutoCLI API')

# URLs registration:
urlpatterns = [
    # Django admin registration:
    path('admin/', admin.site.urls),

    # Swagger view:
    path('api/docs/', schema_view),

    # Inventory/device registration:
    path('network/test/', include('network.inventory.urls')),
    path('api/inventory/', include('network.inventory.api.urls')),

    # Rest framework registration:
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api-token-auth/', obtain_auth_token),
]
