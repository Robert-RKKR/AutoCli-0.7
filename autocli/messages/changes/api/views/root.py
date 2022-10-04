# Rest framework import:
from rest_framework.routers import APIRootView


# Root API view:
class ChangeLogRootView(APIRootView):
    """
    Change Log API root view.
    """
    def get_view_name(self):
        return 'api-changes'
