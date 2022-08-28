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

    # Network/inventory view registration:
    path('network/test/', include('network.inventory.urls')),

    # Network/inventory API view registration:
    path('api/inventory/', include('network.inventory.api.urls')),


    # path('api/inventory/device_type_template/', include('network.inventory.api.urls.device_type_template')),
    # path('api/inventory/device_type/', include('network.inventory.api.urls.device_type')),
    # path('api/inventory/credential/', include('network.inventory.api.urls.credential')),
    # path('api/inventory/device/', include('network.inventory.api.urls.device')),
    # path('api/inventory/group/', include('network.inventory.api.urls.group')),

    # Rest framework registration:
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api-token-auth/', obtain_auth_token),
]
