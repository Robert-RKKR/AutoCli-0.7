# Django import:
from django.contrib import admin

# Log models imports:
from messages.logger.models.extension import Extension
from messages.logger.models.log import Log


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
