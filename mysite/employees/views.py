from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404

from .models import Employee


# Create your views here.
def home(request):
    employees = Employee.objects.all()
    return render(request, 'home.html', {'employees': employees})


def employee_detail(request, employee_id):
    try:
        employees = Employee.objects.get(id=employee_id)
    except Employee.DoesNotExist:
        raise Http404('Employee not found!')
    return render(request, 'employee_detail.html', {'employees': employees})
