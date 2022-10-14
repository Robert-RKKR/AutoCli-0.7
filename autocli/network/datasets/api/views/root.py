# Rest framework import:
from rest_framework.routers import APIRootView


# Root API view:
class DatasetsRootView(APIRootView):
    """
    Datasets API root view.
    """
    def get_view_name(self):
        return 'api-datasets'