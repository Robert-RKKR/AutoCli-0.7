# Content model import:
from messages.content.models.content_type import ContentType

def collect_content_from_name(app_name, model_name):

    try:
        content = ContentType.objects.get(
            app_name=app_name,
            model_name=model_name,
        )
    except:
        return False
    else:
        return content
