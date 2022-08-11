# Django Import:
from django.contrib import admin

# Base Admin Import:
from .base_admin.base_admin import BaseAdmin
from .base_admin.base_simple_admin import BaseSimpleAdmin

# Models Imports:
from inventory.models.credential import Credential
from inventory.models.device_type import DeviceType
from inventory.models.device_type_template import DeviceTypeTemplate
from inventory.models.device import Device
from inventory.models.group import Group


# Admin panel class:
@admin.register(DeviceTypeTemplate)
class DeviceTypeTemplateAdmin(BaseSimpleAdmin):

    list_display = (
        'pk', 'active', 'special', 'vrf', 'device_type', 'command',
    )
    list_filter = (
        'active', 'special', 'vrf', 'device_type',
    )
    search_fields = (
        'command',
    )
    fieldsets = (
        ('Basic information', {
            'classes': ('wide', 'extrapretty',),
            'fields': ('active', 'special', 'vrf',)
        }),
        ('Template information', {
            'classes': ('wide', 'extrapretty',),
            'fields': ('device_type', 'command', 'sfm_expression',),
        }),
    )


@admin.register(Credential)
class CredentialAdmin(BaseAdmin):

    list_display = (
        'pk', 'active', 'name', 'username', 
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
            'fields': ('active', 'name', 'description',)
        }),
        ('Security information', {
            'classes': ('collapse',),
            'fields': ('username', 'password',),
        }),
        ('Additional information', {
            'classes': ('collapse',),
            'fields': ('ico', 'color',),
        }),
    )


@admin.register(DeviceType)
class DeviceTypeAdmin(BaseAdmin):

    list_display = (
        'pk', 'active', 'name', 'netmiko_name', 
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
            'fields': ('active', 'name', 'description', 'netmiko_name',)
        }),
        ('Additional information', {
            'classes': ('collapse',),
            'fields': ('ico', 'color',),
        }),
    )


@admin.register(Device)
class DeviceAdmin(BaseAdmin):

    list_display = (
        'pk', 'active', 'name', 'hostname', 'device_type', 'ssh_status', 'https_status', 'credential',
    )
    list_filter = (
        'active', 'color', 'ssh_status', 'https_status', 'credential',
    )
    search_fields = (
        'name', 'hostname',
    )
    list_select_related = (
        'credential', 'device_type',
    )
    readonly_fields = (
        'root', 'ssh_status', 'https_status',
    )
    fieldsets = (
        ('Basic information', {
            'classes': ('wide', 'extrapretty',),
            'fields': ('active', 'name', 'hostname', 'device_type', 'description',)
        }),
        ('Connection information', {
            'classes': ('wide', 'extrapretty',),
            'fields': ('ssh_port', 'https_port',),
        }),
        ('Status information', {
            'classes': ('collapse',),
            'fields': ('ssh_status', 'https_status',),
        }),
        ('Security information', {
            'classes': ('collapse',),
            'fields': ('credential', 'secret', 'token', 'certificate',),
        }),
        ('Additional information', {
            'classes': ('collapse',),
            'fields': ('ico', 'color',),
        }),
    )


@admin.register(Group)
class GroupAdmin(BaseAdmin):

    list_display = (
        'pk', 'active', 'name', 'root_folder', 
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
            'fields': ('active', 'name', 'description',)
        }),
        ('Devices information', {
            'classes': ('wide', 'extrapretty',),
            'fields': ('devices',),
        }),
        ('Root folder information', {
            'classes': ('wide', 'extrapretty',),
            'fields': ('root_folder',),
        }),
        ('Additional information', {
            'classes': ('collapse',),
            'fields': ('ico', 'color',),
        }),
    )
