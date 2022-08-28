# Django import:
from django.contrib import admin
from django.urls import include
from django.urls import path

# Rest framework import:
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_swagger.views import get_swagger_view

# Main API view import:
from autocli.api.base_view import APIRootView

# Register Swagger view:
schema_view = get_swagger_view(title='AutoCLI API')

# URLs registration:
urlpatterns = [
    # Django admin registration:
    path('admin/', admin.site.urls),

    # Network/inventory view registration:
    path('network/test/', include('network.inventory.urls')),

    # Main API views:
    path('api/token-auth/', obtain_auth_token),
    path('api/docs/', schema_view),
    path('api/', APIRootView.as_view(), name='api-root'),

    # Network/inventory API view registration:
    path('api-inventory/', include('network.inventory.api.urls')),
]
