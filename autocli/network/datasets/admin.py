from django.contrib import admin

# Models import:
from network.datasets.models.device_data import DeviceData

# Register your models here.
admin.site.register(DeviceData)
