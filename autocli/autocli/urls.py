# Django import:
from django.contrib import admin
from django.urls import include
from django.urls import path, re_path

# Rest framework import:
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_swagger.views import get_swagger_view

# Main API view import:
from autocli.api.base_view import APIRootView

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# Register Swagger view:
schema_view = get_schema_view(
    openapi.Info(
        title="AutoCLI API documentation",
        default_version='v0.1',
        description="Welcome to the AutoCLI network automation tool API",
        contact=openapi.Contact(email="robert.kucharski.rkkr@gmail.com"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

# URLs registration:
urlpatterns = [
    # Django admin registration:
    path('admin/', admin.site.urls),

    # Main API views registration:
    path('api/', APIRootView.as_view(), name='api-root'),
    path('api-admin/token-auth/', obtain_auth_token),

    # API documentation views registration:
    re_path(r'^doc(?P<format>\.json|\.yaml)$',
            schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('api-admin/doc/', schema_view.with_ui('swagger', cache_timeout=0),
         name='schema-swagger-ui'),
    path('api-admin/redoc/', schema_view.with_ui('redoc', cache_timeout=0),
         name='schema-redoc'),

    # Network API view registration:
    path('api-inventory/', include('network.inventory.api.urls')),
    path('api-updates/', include('network.updates.api.urls')),

    # Messages API view registration:
    path('api-notification/', include('messages.notifications.api.urls')),
    path('api-changes/', include('messages.changes.api.urls')),
    path('api-log/', include('messages.logger.api.urls')),


    # Network view registration:
    path('network/test/', include('network.inventory.urls')),
]
