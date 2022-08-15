# Django import:
from django.apps import apps

# Collect object base on provided:
#   app name, model name and object ID.
def collect_object(app_name: str, model_name: str, object_id: int):

    collected_model = apps.get_model(
        app_label=app_name,
        model_name=model_name,
    )
    collected_object = collected_model.objects.get(pk=object_id)
    return collected_object
