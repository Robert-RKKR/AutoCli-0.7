# Django Import:
from django.shortcuts import render
from django.core.serializers import serialize
import json

# Application model Import:
from inventory.devices.models.device import Device
from messages.notifications.notification import Notification
from inventory.devices.models.credential import Credential
from messages.logger.models.log import Log

from messages.all.collect import collect_object

# Application models Import:
# from logger.models.log import Log

# Import logger:
from messages.logger.logger import Logger

def test(request):

    # Collect data to display:
    data = {
        'page_title': 'Test RKKR',
        'output': 'Welcome!',
    }

    logger = Logger('Test page')
    device = Device.objects.get(pk=1)
    credentials = Credential.objects.get(pk=1)
    templates = Device.objects.get_device_type_templates(device)




    notification = Notification()
    notification.send('RKKR notification test', **{
        'object': device,
    })
    

    # log1 = logger.debug('Log 1', **{
    #     'object': device,
    #     'code_id': '3747292928490293',
    #     'task_id': 'ISJ@8uw8@*Sh@s2qdijq',
    #     'execution': 394.24,
    # })
    # log2 = logger.debug('Log 2', **{
    #     'object': credentials,
    #     'code_id': '3747292928490293',
    #     'task_id': 'ISJ@8uw8@*Sh@s2qdijq',
    #     'execution': 394.24,
    # })

    json_str = serialize('json', [device], use_natural_foreign_keys=True, use_natural_primary_keys=True)
    data = json.loads(json_str)[0]['fields']

    collected_object = data

    data['output'] = collected_object
    
    # GET method:
    return render(request, 'test.html', data)
