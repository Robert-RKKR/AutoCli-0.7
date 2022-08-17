# Signals import:
from django.db.models.signals import post_save
from django.dispatch import receiver

# Administrator model import:
from django.contrib.auth.models import User

# Post save signal:
@receiver(post_save, sender=User)
def create_user_settings(sender, instance, created, **kwargs):
    if created:
        from system.settings.models.user_setting import UserSetting
        new_user_setting = UserSetting.objects.create(
            administrator=instance,
        )
