# Django import:
from django.contrib import admin

# Change log model import:
from network.updates.models.collected_data import CollectedData
from network.updates.models.snapshot import Snapshot
from network.updates.models.update import Update


# Admin classes:
admin.site.register(CollectedData)
admin.site.register(Snapshot)
admin.site.register(Update)
