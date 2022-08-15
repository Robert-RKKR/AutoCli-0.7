# Django import:
from django.contrib import admin

# Log models imports:
from messages.logger.models.log import Log


@admin.register(Log)
class LogAdmin(admin.ModelAdmin):

    list_display = (
        'pk', 'timestamp', 'application', 'severity', 'task_id', 'message', 'object_id', 'app_name', 'model_name',
    )
    list_filter = (
        'application', 'app_name', 'model_name', 'severity',
    )
    search_fields = (
        'message', 'task_id',
    )
    fieldsets = (
        ('Basic information', {
            'classes': ('wide', 'extrapretty',),
            'fields': ('timestamp', 'severity', 'application', 'task_id',)
        }),
        ('Change object information', {
            'classes': ('wide', 'extrapretty',),
            'fields': ('app_name', 'model_name', 'object_id',),
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
