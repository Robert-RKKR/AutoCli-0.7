# Django import:
from django.contrib import admin

# Notification log model import:
from messages.notifications.models.notification import Notification


@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):

    list_display = (
        'pk', 'timestamp', 'object_id', 'app_name', 'model_name', 'type', 'application', 'message',
    )
    list_filter = (
        'app_name', 'model_name', 'type',
    )
    search_fields = (
        'message',
    )
    fieldsets = (
        ('Basic information', {
            'classes': ('wide', 'extrapretty',),
            'fields': ('type', 'application',)
        }),
        ('Change object information', {
            'classes': ('wide', 'extrapretty',),
            'fields': ('app_name', 'model_name', 'object_id',),
        }),
        ('Message', {
            'classes': ('wide', 'extrapretty',),
            'fields': ('message',),
        }),
    )
