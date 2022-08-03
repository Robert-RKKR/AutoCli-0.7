# Django Import:
from django.contrib import admin

# Model Import:
from testapp.models import TestModel

# Register your models here.
@admin.register(TestModel)
class TestModelAdmin(admin.ModelAdmin):

    list_display = (
        'name', 'test_value', 'description',
    )
    list_filter = (
        'test_value',
    )
    search_fields = (
        'name', 'description',
    )
    fieldsets = (
        ('Basic settings', {
            'classes': ('wide', 'extrapretty',),
            'fields': ('test_value','description', 'name',)
        }),
    )
