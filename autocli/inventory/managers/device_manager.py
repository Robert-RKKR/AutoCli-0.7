# Django Import:
from django.db.models import Manager

# Other models Import:
from inventory.models.device_type_template import DeviceTypeTemplate


# Managers class:
class DeviceManager(Manager):

    def get_device_type_templates(self, device_pk):
        device = self.get(pk=device_pk)
        device_type = device.device_type
        device_type_templates = DeviceTypeTemplate.objects.filter(
            device_type=device_type,
        )
        return device_type_templates
