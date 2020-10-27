from django.http import HttpResponse
from django.urls import path

from main2 import views

urlpatterns = [
    path('', views.index, name='home-main'),
    path('my/<str:city>', views.myCity, name='city'),
    path('home', views.home, name='home'),
    path('student', views.student_list)
]



