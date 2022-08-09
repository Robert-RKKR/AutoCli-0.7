# Django Import
from django.contrib import admin

# Import actions:
from core.base_admin.actions import change_status_to_true
from core.base_admin.actions import change_status_to_false


# Admin class:
class BaseSimpleAdmin(admin.ModelAdmin):

    exclude = ('deleted',)
    readonly_fields = ('root',)
    empty_value_display = '-None-'
    list_display_links = ('pk',)
    list_per_page = 10
    list_max_show_all = 100
    actions = [
        change_status_to_true,
        change_status_to_false
    ]
