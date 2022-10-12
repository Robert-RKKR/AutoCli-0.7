# Django signals import:
from django.db.models.signals import post_save
from django.dispatch import receiver

# Collect settings function import:
from system.settings.settings import collect_setting

# Update models import:
from network.updates.models.update import Update

# Post save signal:
@receiver(post_save, sender=Update)
def post_save_update_signal(sender, instance=None, created=False, **kwargs):
    """
    Check that the number of existing upgrade models belonging to
    one network device, is not higher than allowed (Specified in the settings).
    Updates that belong to snapshot are not counted.
    """

    # Collect default value:
    history_length = collect_setting('history_length', default=5)

    # Check current amount of existing updates that match criteria:
    if created:
        try:
            match_updates = sender.objects.filter(
                device=instance.device,
                snapshot=None).order_by('-id')
            if len(match_updates) > history_length:
                # Delate oldest update:
                for to_delete in match_updates[history_length:]:
                    to_delete.delete()
        except:
            pass
