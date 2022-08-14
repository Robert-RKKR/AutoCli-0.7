# Django signals Import:
from django.db.models.signals import pre_save, post_save
from django.forms.models import model_to_dict
from django.dispatch import receiver

# Application change log Import:
from messages.content.models.content_type import ContentType
from messages.changes.models.change_log import ChangeLog

# Application model Import:
from inventory.models.credential import Credential

# Post save signal:
@receiver(post_save)
def base_post_signal(sender, instance=None, created=False, **kwargs):
    try:
        # Collect change log content type:
        content_type = ContentType.objects.get(
            app_name=sender._meta.app_label,
            model_name=sender.__name__,
        )
    except: # Pass if sender was not register:
        pass
    else: # Create change log if sender was register:
        change_log_action = 0
        # Check if object was created
        if created:
            change_log_action = 1
        else:
            change_log_action = 2
        # Create a new change log:
        change_log = ChangeLog.objects.create(
            action=change_log_action,
            content_type=content_type,
            object_id=instance.pk,
            after=model_to_dict(instance),
        )

# @receiver(post_save)
# def base_post_signal(sender, instance, created, **kwargs):
#     change_log_action = 0
#     # Check if object was created
#     if created:
#         change_log_action = 1
#     else:
#         change_log_action = 2
#     # Create a new change log content type:
#     content_type = ContentType.objects.create(
#         app_name='inventory',
#         model_name='Credential',
#     )
#     # Create a new change log:
#     change_log = ChangeLog.objects.create(
#         action=change_log_action,
#         content_type=content_type,
#         object_id=instance.pk,
#         after=model_to_dict(instance),
#     )


# @receiver(post_save) # instead of @receiver(post_save, sender=Rebel)
# def set_winner(sender, instance=None, created=False, **kwargs):
#     list_of_models = ('Rebel', 'Stormtrooper', 'Battleground')
#     if sender.__name__ in list_of_models: # this is the dynamic part you want
#         if created: # only run when object is first created
#             ... set the winner ...
