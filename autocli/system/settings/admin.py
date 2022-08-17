# Django import:
from django.contrib import admin

# Change log model import:
from system.settings.models.user_setting import UserSetting
from system.settings.models.setting import Setting


admin.site.register(UserSetting)
admin.site.register(Setting)
