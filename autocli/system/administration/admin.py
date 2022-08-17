# Django import:
from django.contrib import admin

# Change log model import:
from system.administration.models.administrator import Administrator


@admin.register(Administrator)
class AdministratorAdmin(admin.ModelAdmin):

    list_display = (
        'pk', 'name', 'is_active', 'is_superuser', 'is_staff', 'email',
    )
    list_filter = (
        'is_active', 'is_staff',
    )
    search_fields = (
        'name',
    )
    fieldsets = (
        ('Basic information', {
            'classes': ('wide', 'extrapretty',),
            'fields': ('name', 'email',)
        }),
        ('Status information', {
            'classes': ('wide', 'extrapretty',),
            'fields': ('is_active', 'is_staff', 'is_superuser',)
        }),
        ('Permissions information', {
            'classes': ('wide', 'extrapretty',),
            'fields': ('groups',)
        }),
        ('Login information', {
            'classes': ('wide', 'extrapretty',),
            'fields': ('last_login',)
        }),
    )
