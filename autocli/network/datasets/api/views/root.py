# Rest framework import:
from rest_framework.routers import APIRootView


# Root API view:
class UpdatesRootView(APIRootView):
    """
    Updates API root view.
    """
    def get_view_name(self):
        return 'api-updates'
