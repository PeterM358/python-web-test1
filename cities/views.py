from django.shortcuts import render

# from djangoStart.models import Person
from djangoStart.cities.models import Person


def index(req):
    context = {
        'name': 'Koki',
        'people': Person.objects.all(),
    }
    return render(req, 'index.html', context)
