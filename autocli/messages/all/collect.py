# Django import:
from django.apps import apps

# Collect object base on provided:
#   app name, model name and object ID.
def collect_object(app_name: str, model_name: str, object_id: int):

    # try to collect model based on app and model name:
    try:
        collected_model = apps.get_model(
            app_label=app_name,
            model_name=model_name,
        )
    except:
        # In case of model collection problem, return false:
        return False
    else:
        # Try to collect object based on object ID:
        try:
            collected_object = collected_model.objects.get(pk=object_id)
        except:
            # In case of object collection problem, return false:
            return False
        else:
            # Return collected object:
            return collected_object
