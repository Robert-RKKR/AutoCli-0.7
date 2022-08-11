# Django Import:
from django.db.utils import OperationalError

# Application change log Import:
from core.models.content_type import ContentType

# Follow function:
def follow_change_log(model):

    # Try to register new model if not exist:
    try:
        all_content_types = ContentType.objects.get_or_create(
            app_name=model._meta.app_label,
            model_name=model.__name__,
        )
    except OperationalError:
        pass
