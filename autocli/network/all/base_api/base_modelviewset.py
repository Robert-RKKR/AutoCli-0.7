# Rest framework import:
from rest_framework import viewsets


# Base ModelViewSet model:
class BaseModelViewSet(viewsets.ModelViewSet):
    """
    Xxx.
    """

    def get_own_serializer_class(self, many=True):

        # Collect class:
        if many:
            return self.serializer_class
        else:
            try:
                # Try to collect single serializer class:
                return self.single_serializer_class
            except:
                # use default serializer class:
                return self.serializer_class


    def create(self, *args, **kwargs):
        self.serializer_class = self.get_own_serializer_class(many=False)
        return viewsets.ModelViewSet.create(self, *args, **kwargs)

    def update(self, *args, **kwargs):
        self.serializer_class = self.get_own_serializer_class(many=False)
        return viewsets.ModelViewSet.update(self, *args, **kwargs)

    def list(self, *args, **kwargs):
        self.serializer_class = self.get_own_serializer_class(many=True)
        return viewsets.ModelViewSet.list(self, *args, **kwargs)

    def retrieve(self, *args, **kwargs):
        self.serializer_class = self.get_own_serializer_class(many=True)
        return viewsets.ModelViewSet.retrieve(self, *args, **kwargs)

