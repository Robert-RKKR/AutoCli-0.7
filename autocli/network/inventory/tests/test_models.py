# Django import:
from django.test import TestCase

# Models import:
from network.inventory.models.device_type_template import DeviceTypeTemplate
from network.inventory.models.device_type import DeviceType
from network.inventory.models.credential import Credential
from network.inventory.models.device import Device
from network.inventory.models.group import Group

# Taste case classes:
class TestModels(TestCase):

    @classmethod
    def setUp(cls):

        device_types = [
            DeviceType.objects.create(name='Cisco IOS', netmiko_name='cisco_ios'),
            DeviceType.objects.create(name='Cisco IOS XE', netmiko_name='cisco_iosxe'),
        ]

        device_type_templates = [
            DeviceTypeTemplate.objects.create(command='show version', sfm_expression='Test1', device_type=device_types[0], vrf=True, special=True),
            DeviceTypeTemplate.objects.create(command='show interfaces', sfm_expression='Test2', device_type=device_types[0], vrf=True, special=True),
            DeviceTypeTemplate.objects.create(command='show ip route', sfm_expression='Test3', device_type=device_types[1], vrf=True, special=True),
            DeviceTypeTemplate.objects.create(command='show clock', sfm_expression='Test4', device_type=device_types[1], vrf=True, special=True),
        ]

        credentials = [
            Credential.objects.create(name='Admin', username='admin', password='!Cisco123'),
            Credential.objects.create(name='SuperAdmin', username='superadmin', password='!Cisco123'),
        ]

        root_groups = [
            Group.objects.create(name='CH'),
        ]

        groups = [
            Group.objects.create(name='CHSTH', root_folder=root_groups[0]),
            Group.objects.create(name='CHBAR', root_folder=root_groups[0]),
            Group.objects.create(name='CHZRH', root_folder=root_groups[0]),
        ]

        devices = [
            Device.objects.create(name='chsthrtrlab1', hostname='10.1.1.1', device_type=device_types[0], credential=credentials[1]),
            Device.objects.create(name='chbarrtrlab1', hostname='10.2.1.1', device_type=device_types[1], credential=credentials[0]),
            Device.objects.create(name='chzrhrtrlab1', hostname='10.3.1.1', device_type=device_types[1], credential=credentials[1]),
        ]

        groups[1].devices.set([devices[0]])
        groups[1].devices.set([devices[1]])
        groups[1].devices.set([devices[2]])

    def test_device(self):
        device = Device.objects.get(pk=1)
        self.assertEqual(device.name, 'chsthrtrlab1')

    def test_device_credentials(self):
        device = Device.objects.get(pk=2)
        self.assertEqual(device.credential.name, 'Admin')
