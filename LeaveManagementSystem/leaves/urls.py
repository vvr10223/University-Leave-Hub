from django.contrib import admin
from django.urls import path,include
from .views import *
urlpatterns = [
    path('principal_dashboard/',principal_dashboard,name='principal_dashboard'),
    path('hod_dashboard/',hod_dashboard,name='hod_dashboard'),
    path('employee_dashboard/',employee_dashboard,name='employee_dashboard'),
]
