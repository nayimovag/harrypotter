from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from main2.models import Student


def index(request):
    return HttpResponse("Hello")


def myCity(request, city):
    return HttpResponse(f'You are from {city}')


def home(request):
    return render(request, 'index.html')


def student_list(request):
    data = Student.objects.all()
    return render(request, 'student.html', {"data": data})
