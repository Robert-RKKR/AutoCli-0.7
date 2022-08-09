# Django Import:
from django.shortcuts import render

# Application model Import:
from inventory.models.device import Device

# Import logger:
from logger.logger import Logger

def test(request):

    # Collect data to display:
    data = {
        'page_title': 'Test RKKR',
        'output': 'Welcome!',
    }

    logger = Logger('Test page')
    logger.debug('Hello world!', **{
        'correlated': 'chsthrtr-123',
        'code_id': '3747292928490293',
        'task_id': 'ISJ@8uw8@*Sh@s2qdijq',
        'execution': 394.24,
        'additional information': 'This is a message from another world.'
    })

    device = Device.objects.get_device_type_templates(device_pk=1)

    data['output'] = device
    
    # GET method:
    return render(request, 'test.html', data)
