import json
from django.shortcuts import render
from django.core.serializers import serialize
from network.inventory.models.device import Device
from messages.notifications.notification import Notification
from network.inventory.models.credential import Credential
from network.inventory.models.device_type_template import DeviceTypeTemplate
from messages.logger.models.log import Log
from messages.logger.logger import Logger
from network.all.base_connection.connection import Connection
from network.all.base_connection.connections import Connections
from system.settings.settings import collect_setting
from network.inventory.tasks.check_device_status_task import CheckDeviceStatus
from network.updates.tasks.collect_device_data_task import CollectDeviceDataTask
from network.updates.models.update import Update

def test(request):

    # Collect data to display:
    data = {
        'page_title': 'Test RKKR',
        'output': 'Welcome!',
    }

    logger = Logger('Test page')
    log = logger.critical('================================')

    # data['output'] = CollectDeviceDataTask([1])
    # data['output'] = CheckDeviceStatus([1, 22])

    device = Device.objects.get(pk=1)
    # devices = Device.objects.filter(pk__in=[1, 22])
    # all_devices = Device.objects.all()

    # with Connection(device) as con:
    #     output = con.send_enabled_dict([
    #         'show version',
    #         # 'show ip route',
    #         # 'show ip access-list',
    #         # 'show psp',
    #         # 'show cdp neighbors detail',
    #         # 'show clock',
    #         # 'show network'
    #     ])

    # with Connections(devices) as con:
    #     output = con.send_enable([
    #         'show version',
    #         'show ip route',
    #         'show ip access-list',
    #         'show psp',
    #         'show cdp neighbors detail',
    #         'show clock',
    #         'show network'
    #     ])

    # with Connections(devices) as con:
    #     output = con.execute_device_type_templates()

    criteria = Update.objects.order_by().values('device').distinct()
    # Update.objects.filter(
    #     device=device,
    # ).latest('created')

    # to_delete.delete()

    # data['output'] = json.dumps(output)
    data['output'] = criteria
    
    # GET method:
    return render(request, 'test.html', data)
