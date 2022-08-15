# Django Import:
from django.db.utils import OperationalError

content_types = []

# Follow function:
def follow_change_log(model):

    # Try to register new model if not exist:
    content_type = (model._meta.app_label, model.__name__)
    if not content_type in content_types:
        content_types.append(content_type)
