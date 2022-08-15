# Django signals import:
from django.db.models.signals import post_save
from django.forms.models import model_to_dict
from django.dispatch import receiver

# Application change log import:
from messages.changes.models.change_log import ChangeLog

# Content type import:
from .follow_change_log import content_types

# Post save signal:
# @receiver(post_save)
def base_post_signal(sender, instance=None, created=False, **kwargs):
    
    change_log_action = 0
    # Check if object was created
    if created:
        change_log_action = 1
    else:
        change_log_action = 2

    # Collect base content type information:
    try:
        app_name = sender._meta.app_label
        model_name = sender.__name__
    except:
        app_name = None
        model_name = None
    
    if (app_name, model_name) in content_types:
        try:
            # Create a new change log:
            ChangeLog.objects.create(
                action=change_log_action,
                app_name=sender._meta.app_label,
                model_name=sender.__name__,
                object_id=instance.pk,
                after=model_to_dict(instance),
            )
        except: # Pass if sender was not register:
            pass
