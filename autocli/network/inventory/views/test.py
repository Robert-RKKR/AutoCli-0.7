# Django Import:
from django.shortcuts import render
from django.core.serializers import serialize
import json

# Application model Import:
from network.inventory.models.device import Device
from messages.notifications.notification import Notification
from network.inventory.models.credential import Credential
from network.inventory.models.device_type_template import DeviceTypeTemplate
from messages.logger.models.log import Log
from messages.logger.logger import Logger
from network.all.base_connection.connection import Connection
from system.settings.settings import collect_setting

def test(request):

    # Collect data to display:
    data = {
        'page_title': 'Test RKKR',
        'output': 'Welcome!',
    }

    logger = Logger('Test page')
    log = logger.critical('================')

    device = Device.objects.get(pk=1)

    with Connection(device) as con:
        data['output'] = con.send_enable([
            'show version',
            'show ip route',
            'show ip access-list',
            'show psp'
        ])
    
    # GET method:
    return render(request, 'test.html', data)
