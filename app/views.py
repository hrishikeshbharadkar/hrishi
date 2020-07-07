from django.shortcuts import render
from .models import myinfo, job, job_desc


def index(request):
    obj = job.objects.all()
    obj1 = job_desc.objects.all()
    obj2 = myinfo.objects.all()
    context = {
        'object': obj,
        'object1': obj1,
        'object2': obj2,
    }
    return render(request, 'index.html', context)
