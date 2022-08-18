# Base manager import:
from inventory.all.base_model.all.managers import BaseManager

# Other models Import:
from inventory.devices.models.device_type_template import DeviceTypeTemplate


# Managers class:
class DeviceManager(BaseManager):

    def get_device_type_templates(self, device):
        device_type = device.device_type
        device_type_templates = DeviceTypeTemplate.objects.filter(
            device_type=device_type,
        )
        return device_type_templates

    def get_device_type_templates_from_pk(self, device_pk: int):
        device = self.get(pk=device_pk)
        device_type = device.device_type
        device_type_templates = DeviceTypeTemplate.objects.filter(
            device_type=device_type,
        )
        return device_type_templates

    def get_by_natural_key(self, name):
        return self.get(name=name)
