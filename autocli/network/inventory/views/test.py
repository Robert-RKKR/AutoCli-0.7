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
from network.all.base_connection.base_connection import BaseConnection
from system.settings.settings import collect_setting

def test(request):

    # Collect data to display:
    data = {
        'page_title': 'Test RKKR',
        'output': 'Welcome!',
    }

    # connection = BaseConnection()

    data['output'] = collect_setting('default_username')
    
    # GET method:
    return render(request, 'test.html', data)
