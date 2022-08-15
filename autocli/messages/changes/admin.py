# Django import:
from django.contrib import admin

# Change log model import:
from messages.changes.models.change_log import ChangeLog


@admin.register(ChangeLog)
class ChangeLogAdmin(admin.ModelAdmin):

    list_display = (
        'pk', 'timestamp', 'action', 'app_name', 'model_name', 'object_id', 'administrator',
    )
    list_filter = (
        'administrator', 'action', 'app_name', 'model_name',
    )
    search_fields = (
        'object_id',
    )
    fieldsets = (
        ('Basic information', {
            'classes': ('wide', 'extrapretty',),
            'fields': ('action', 'administrator',)
        }),
        ('Change object information', {
            'classes': ('wide', 'extrapretty',),
            'fields': ('app_name', 'model_name', 'object_id',),
        }),
        ('Change information', {
            'classes': ('wide', 'extrapretty',),
            'fields': ('after',),
        }),
    )
