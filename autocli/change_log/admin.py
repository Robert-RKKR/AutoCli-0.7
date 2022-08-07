# Django Import:
from django.contrib import admin

# Models Imports:
from change_log.models.content_type import ContentType
from change_log.models.change_log import ChangeLog


# Admin panel class:
@admin.register(ChangeLog)
class ChangeLogAdmin(admin.ModelAdmin):

    list_display = (
        'pk', 'action', 'administrator', 'object_id',
    )
    list_filter = (
        'administrator', 'action',
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
            'fields': ('action', 'administrator',)
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
