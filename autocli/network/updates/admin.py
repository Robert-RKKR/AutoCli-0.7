# Django import:
from django.contrib import admin

# Base Admin Import:
from network.all.base_admin.base_admin import BaseAdmin

# Change log model import:
from network.updates.models.collected_data import CollectedData
from network.updates.models.snapshot import Snapshot
from network.updates.models.update import Update


# Admin classes:
@admin.register(CollectedData)
class CollectedDataAdmin(BaseAdmin):

    list_display = (
        'pk', 'active', 'result_status', 'raw_data_status', 'processed_data_status', 'update',
    )
    list_filter = (
        'active', 'result_status', 'raw_data_status', 'processed_data_status',
    )
    search_fields = (
        'command_name',
    )
    readonly_fields = (
        'root', 'result_status', 'raw_data_status', 'processed_data_status',
    )
    fieldsets = (
        ('Basic status information', {
            'classes': ('wide', 'extrapretty',),
            'fields': ('active', 'result_status', 'raw_data_status', 'processed_data_status',)
        }),
        ('Basic information', {
            'classes': ('wide', 'extrapretty',),
            'fields': ('update', 'command_name', 'command_raw_data', 'command_processed_data',)
        }),
    )

    
@admin.register(Snapshot)
class SnapshotAdmin(BaseAdmin):

    list_display = (
        'pk', 'active', 'name',
    )
    list_filter = (
        'active',
    )
    fieldsets = (
        ('Basic information', {
            'classes': ('wide', 'extrapretty',),
            'fields': ('active', 'name', 'description',)
        }),
    )


@admin.register(Update)
class UpdateAdmin(BaseAdmin):

    list_display = (
        'pk', 'active', 'device', 'snapshot', 'result_status',
    )
    list_filter = (
        'active', 'snapshot', 'result_status', 'device',
    )
    fieldsets = (
        ('Basic information', {
            'classes': ('wide', 'extrapretty',),
            'fields': ('active', 'device', 'snapshot', 'result_status',)
        }),
    )
