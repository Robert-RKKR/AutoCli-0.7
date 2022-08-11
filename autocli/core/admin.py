# Django Import:
from django.contrib import admin

# Models Imports:
from core.models.content_type import ContentType


# Admin panel class:
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
