# Django Import:
from django.contrib import admin

# Models Imports:
from logger.models.extension import Extension
from logger.models.log import Log


# Admin panel class:
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
            'fields': ('Data',)
        }),
    )


@admin.register(Log)
class LogAdmin(admin.ModelAdmin):

    list_display = (
        'pk', 'application', 'severity', 'correlated_object', 'task_id', 'message',
    )
    list_filter = (
        'application', 'correlated_object', 'severity',
    )
    search_fields = (
        'message', 'task_id',
    )
    readonly_fields = (
        'application', 'correlated_object', 'task_id', 'severity', 'message', 'code_id', 'execution_time', 'timestamp',
    )
    fieldsets = (
        ('Basic information', {
            'classes': ('wide', 'extrapretty',),
            'fields': ('timestamp', 'severity', 'application', 'correlated_object', 'task_id',)
        }),
        ('Message', {
            'classes': ('wide', 'extrapretty',),
            'fields': ('message',),
        }),
        ('Additional information', {
            'classes': ('collapse',),
            'fields': ('code_id', 'execution_time'),
        }),
    )
