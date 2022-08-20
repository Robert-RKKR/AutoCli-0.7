# Django Import:
from django.contrib import admin

# Base Admin Import:
from inventory.all.base_admin.base_admin import BaseAdmin

# Tag model import:
from inventory.tags.models.tag import Tag


# Admin panel class:
@admin.register(Tag)
class TagAdmin(BaseAdmin):

    list_display = (
        'pk', 'active', 'name', 'color', 
    )
    list_filter = (
        'active', 'color', 
    )
    search_fields = (
        'name',
    )
    fieldsets = (
        ('Basic information', {
            'classes': ('wide', 'extrapretty',),
            'fields': ('active', 'name', 'description', 'color')
        }),
    )
