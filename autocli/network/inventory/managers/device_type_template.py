# Base manager import:
from network.all.base_model.managers.base_manager import BaseManager


# Managers class:
class DeviceTypeTemplateManager(BaseManager):

    def get_by_natural_key(self, command, device_type):
        return self.get(command=command, device_type=device_type)
