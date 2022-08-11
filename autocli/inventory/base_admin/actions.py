# Django Import
from django.contrib import admin

# Actions:
@admin.action(description='Change status to active')
def change_status_to_true(modeladmin, request, queryset):
    queryset.update(active=True)

@admin.action(description='Change status to passive')
def change_status_to_false(modeladmin, request, queryset):
    queryset.update(active=False)
