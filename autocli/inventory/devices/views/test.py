# Django Import:
from django.shortcuts import render

# Application model Import:
from inventory.devices.models.device import Device

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
    log = logger.debug('Hello world!', **{
        'object_id': 123,
        'code_id': '3747292928490293',
        'task_id': 'ISJ@8uw8@*Sh@s2qdijq',
        'execution': 394.24,
    })

    
    device = Device.objects.get(pk=1)
    templates = Device.objects.get_device_type_templates(device)

    data['output'] = templates
    
    # GET method:
    return render(request, 'test.html', data)
