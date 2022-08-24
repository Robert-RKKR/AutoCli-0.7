# Rest framework import:
from rest_framework import viewsets


# Base ModelViewSet model:
class BaseModelViewSet(viewsets.ModelViewSet):
    """
    Xxx.
    """

    def create(self, *args, **kwargs):
        self.serializer_class = self.create_serializer_class
        return viewsets.ModelViewSet.create(self, *args, **kwargs)

    # def list(self, *args, **kwargs):
    #     self.serializer_class = self.list_serializer_class
    #     return viewsets.ModelViewSet.create(self, *args, **kwargs)

