# Django import:
from django.contrib import admin

# Change log model import:
from messages.changes.models.change_log import ChangeLog


@admin.register(ChangeLog)
class ChangeLogAdmin(admin.ModelAdmin):

    list_display = (
        'pk', 'timestamp', 'action', 'content_type', 'object_id', 'administrator',
    )
    list_filter = (
        'administrator', 'action', 'content_type',
    )
    search_fields = (
        'object_id',
    )
    list_select_related = (
        'content_type',
    )
    readonly_fields = (
        'action', 'administrator', 'content_type', 'object_id', 'after',
    )
    fieldsets = (
        ('Basic information', {
            'classes': ('wide', 'extrapretty',),
            'fields': ('timestamp', 'action', 'administrator',)
        }),
        ('Change object information', {
            'classes': ('wide', 'extrapretty',),
            'fields': ('content_type', 'object_id',),
        }),
        ('Change information', {
            'classes': ('wide', 'extrapretty',),
            'fields': ('after',),
        }),
    )
