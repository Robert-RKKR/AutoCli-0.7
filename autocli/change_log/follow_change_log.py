# Application change log Import:
from change_log.models.content_type import ContentType

# Follow function:
def follow_change_log(model):

    # Register new model if not exist:
    all_content_types = ContentType.objects.get_or_create(
        app_name=model._meta.app_label,
        model_name=model.__name__,
    )
