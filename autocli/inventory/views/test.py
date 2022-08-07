# Django Import:
from django.shortcuts import render

# Application model Import:
from inventory.models.device import Device

def test(request):

    # Collect data to display:
    data = {
        'page_title': 'Test RKKR',
        'output': 'Welcome!',
    }

    device = Device.objects.get_device_type_templates(device_pk=1)

    data['output'] = device
    
    # GET method:
    return render(request, 'test.html', data)
