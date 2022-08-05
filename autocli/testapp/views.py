# Django Import:
from django.shortcuts import render
import threading

# Application Import:
from change_log.models import ChangeLog

def test(request):

    # Collect data to display:
    data = {
        'page_title': 'Test RKKR',
        'output': 'Welcome!',
    }

    before_change = ChangeLog.objects.filter(
        model_name='TestModel',
        object_name='Change log test'
    ).order_by('updated').first()
    after_change = ChangeLog.objects.filter(
        model_name='TestModel',
        object_name='Change log test'
    ).latest('updated')

    # data['output'] = before_change
    data['before_change'] = before_change
    data['after_change'] = after_change
    
    # GET method:
    return render(request, 'test.html', data)
