# Django import:
from django.contrib import admin

# Change log model import:
from system.administration.models.administrator import Administrator


admin.site.register(Administrator)
# @admin.register(Administrator)
# class AdministratorAdmin(admin.ModelAdmin):

#     list_display = (
#         'pk', 'name', 'is_active', 'is_staff', 'email',
#     )
#     list_filter = (
#         'is_active', 'is_staff',
#     )
#     search_fields = (
#         'name',
#     )
#     fieldsets = (
#         ('Basic information', {
#             'classes': ('wide', 'extrapretty',),
#             'fields': ('name', 'is_active', 'is_staff', 'email',)
#         }),
#     )
