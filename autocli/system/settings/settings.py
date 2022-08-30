# Settings models import:
from system.settings.models.user_setting import UserSetting
from system.settings.models.setting import Setting

# Administrator model import:
from django.contrib.auth.models import User

# Settings functions:
def collect_user_settings(user: User) -> UserSetting:
    """
    Collect user settings from database.
    """

    if isinstance(user, User):
        try: # Try to collect user settings:
            return UserSetting.objects.get(
                administrator = user,
            )
        except: # Return False if user settings do not exist:
            return False
    else:
        return False

def collect_main_settings() -> Setting:
    """
    Collect main settings.
    """
    try: # Try to collect main settings:
        return Setting.objects.get(current=True)
    except: # Return False if user settings do not exist:
        return False

def collect_setting(setting_value: str, user: User = None, default = None):
    """
    Collect setting data based on provided value from database:
    1. Collect setting from user settings (If provided).
    2. Collect setting from main settings.
    3. Provided default value.
    """

    # Check if setting_value is valid:
    if not isinstance(setting_value, str):
        raise TypeError('The given setting_value is not a string.')

    # Check if user was provided:
    if user:
        # Collect user settings from database:
        user_settings = collect_user_settings(user)
    else:
        user_settings = None
    # Define return value:
    collected_data = None
    # If user settings was collected:
    if user_settings or user_settings is None:
        try: # Try to collect user settings data:
            collected_data = getattr(user_settings, setting_value)
        except: # If there is no user settings data:
            # Collect current main settings:
            main_settings = collect_main_settings()
            if main_settings:
                try: # try to collect main settings data:
                    collected_data = getattr(main_settings, setting_value)
                except: # If there is no main settings data:
                    # Use provided default value:
                    collected_data = default

    # Return collected data:
    return collected_data
