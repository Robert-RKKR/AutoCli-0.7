# Django import:
from django.contrib import admin

# Content type model import:
from message_system.models_content.content_type import ContentType

# Notification log model import:
from message_system.models_notification.notification import Notification

# Change log model import:
from message_system.models_change.change_log import ChangeLog

# Log models imports:
from message_system.models_log.extension import Extension
from message_system.models_log.log import Log


# NOTIFICATION CONTENT TYPE:
@admin.register(ContentType)
class ContentTypeAdmin(admin.ModelAdmin):

    list_display = (
        'pk', 'app_name', 'model_name',
    )
    readonly_fields = (
        'app_name', 'model_name',
    )
    fieldsets = (
        ('Basic information', {
            'classes': ('wide', 'extrapretty',),
            'fields': ('app_name', 'model_name',)
        }),
    )


# NOTIFICATION LOG ADMIN:
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


# CHANGE LOG ADMIN:
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


#  LOG ADMIN:
@admin.register(Extension)
class ExtensionAdmin(admin.ModelAdmin):

    list_display = (
        'pk', 'log', 'name',
    )
    readonly_fields = (
        'log', 'name', 'data',
    )
    fieldsets = (
        ('Basic information', {
            'classes': ('wide', 'extrapretty',),
            'fields': ('log', 'name',)
        }),
        ('Data', {
            'classes': ('wide', 'extrapretty',),
            'fields': ('data',)
        }),
    )


@admin.register(Log)
class LogAdmin(admin.ModelAdmin):

    list_display = (
        'pk', 'timestamp', 'application', 'severity', 'object_id', 'task_id', 'message',
    )
    list_filter = (
        'application', 'content_type', 'severity',
    )
    search_fields = (
        'message', 'task_id',
    )
    readonly_fields = (
        'application', 'object_id', 'task_id', 'severity', 'message', 'code_id', 'execution', 'timestamp',
    )
    fieldsets = (
        ('Basic information', {
            'classes': ('wide', 'extrapretty',),
            'fields': ('timestamp', 'severity', 'application', 'task_id',)
        }),
        ('Change object information', {
            'classes': ('wide', 'extrapretty',),
            'fields': ('content_type', 'object_id',),
        }),
        ('Message', {
            'classes': ('wide', 'extrapretty',),
            'fields': ('message',),
        }),
        ('Additional information', {
            'classes': ('collapse',),
            'fields': ('code_id', 'execution'),
        }),
    )
