# Django Import:
from django.shortcuts import render

# Application model Import:
from inventory.models.device import Device

# Application models Import:
from logger.models.log import Log

# Import logger:
from logger.logger import Logger

def test(request):

    # Collect data to display:
    data = {
        'page_title': 'Test RKKR',
        'output': 'Welcome!',
    }

    logger = Logger('Test page')
    log = logger.debug('Hello world!', **{
        'correlated': 'chsthrtr-123',
        'code_id': '3747292928490293',
        'task_id': 'ISJ@8uw8@*Sh@s2qdijq',
        'execution': 394.24,
        'additional information11': 'This is a message from another world.',
        'additional information12': 'This is a message from another world.',
        'additional information21': 'This is a message from another world.',
        'additional information22': 'This is a message from another world.',
        'additional information31': 'This is a message from another world.',
        'additional information32': 'This is a message from another world.',
    })

    

    device = Device.objects.get_device_type_templates(1)

    data['output'] = Log.objects.get_log_extensions(log)
    
    # GET method:
    return render(request, 'test.html', data)
