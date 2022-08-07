# Django Import:
from django.shortcuts import render

def test(request):

    # Collect data to display:
    data = {
        'page_title': 'Test RKKR',
        'output': 'Welcome!',
    }
    
    # GET method:
    return render(request, 'test.html', data)
