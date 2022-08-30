# Django signals import:
from django.db.models.signals import post_save
from django.dispatch import receiver

# Settings models import:
from system.settings.models.setting import Setting

# Administrator model import:
from django.contrib.auth.models import User

# Post save signals:
@receiver(post_save, sender=User)
def create_user_settings(sender, instance, created, **kwargs):
    if created:
        from system.settings.models.user_setting import UserSetting
        new_user_setting = UserSetting.objects.create(
            administrator=instance,
        )

@receiver(post_save, sender=Setting)
def current_settings(sender, instance=None, created=False, **kwargs):
    """
    If new or changed settings object have current value set to True,
    all oder settings object should have value current set to False.
    """

    # Collect object current value:
    current_value = instance.current
    # If current value is True change previous current setting to False:
    if current_value:

        # Try to collect current settings object:
        try:
            current_settings = Setting.objects.filter(current=True)
        except:
            current_settings = False

        if current_settings:
            # Iterate thru collected current settings:
            for setting in current_settings:
                
                # Check that the current settings is not the same object,
                # that sent the signal:
                if setting != instance:
                    setting.current = False
                    setting.save(update_fields=['current'])
