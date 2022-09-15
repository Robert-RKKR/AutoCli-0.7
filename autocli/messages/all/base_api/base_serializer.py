# Rest framework import:
from rest_framework import serializers


# Base serializer:
class BaseSerializer(serializers.HyperlinkedModelSerializer):

    base_fields = [
        'pk',
        'url',
        'timestamp',
        'app_name',
        'model_name',
        'object_id',
    ]
