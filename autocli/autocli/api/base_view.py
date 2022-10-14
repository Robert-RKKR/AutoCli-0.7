# Rest framework import:
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.views import APIView


# Main API view:
class APIRootView(APIView):
    """
    This is the root of AutoCLI REST API.
    """
    _ignore_model_permissions = True
    exclude_from_schema = True
    swagger_schema = None

    def get_view_name(self):
        return "API Root"

    def get(self, request, format=None):

        return Response({
            'inventory': reverse('api-inventory:api-root', request=request, format=format),
            'updates': reverse('api-updates:api-root', request=request, format=format),
            'datasets': reverse('api-datasets:api-root', request=request, format=format),
            'changes': reverse('api-changes:api-root', request=request, format=format),
            'logger': reverse('api-logger:api-root', request=request, format=format),
            'notifications': reverse('api-notifications:api-root', request=request, format=format),
        })
