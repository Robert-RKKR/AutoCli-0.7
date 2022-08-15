# PyTest import:
from unicodedata import name
import pytest

# Application model Import:
from inventory.devices.models.device import Device
from messages.logger.models.log import Log

# Logger import:
from messages.logger.logger import Logger

# @pytest.mark.django_db
# def test_device_creation():
#     pass

@pytest.mark.django_db
def test_first():
    device = Device.objects.create(
        name='Test device name',
        hostname='192.168.1.1',
    )
    logger = Logger('Test')
    log = logger.debug('Test log', **{
        'object': device,
        'code_id': '3747292928490293',
        'task_id': 'ISJ@8uw8@*Sh@s2qdijq',
        'execution': 394.24,
    })
    print(device, log)

    assert isinstance(log, Log)
