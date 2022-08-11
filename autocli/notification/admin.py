# Django Import:
from django.contrib import admin

# Models Imports:
from notification.models.notification import Notification


# Admin panel class:
@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):

    list_display = (
        'pk', 'timestamp', 'object_id', 'type', 'message',
    )
    list_filter = (
        'content_type', 'type',
    )
    search_fields = (
        'message',
    )
    readonly_fields = (
        'object_id', 'message', 'timestamp', 'type', 'content_type', 
    )
    fieldsets = (
        ('Basic information', {
            'classes': ('wide', 'extrapretty',),
            'fields': ('timestamp', 'type',)
        }),
        ('Change object information', {
            'classes': ('wide', 'extrapretty',),
            'fields': ('content_type', 'object_id',),
        }),
        ('Message', {
            'classes': ('wide', 'extrapretty',),
            'fields': ('message',),
        }),
    )
