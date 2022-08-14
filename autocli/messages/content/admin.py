# Django import:
from django.contrib import admin

# Content type model import:
from messages.content.models.content_type import ContentType


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
