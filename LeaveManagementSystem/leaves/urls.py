from django.contrib import admin
from django.urls import path,include
from .views import *
urlpatterns = [
    path('leave_application/',leaveApplication,name='leave_application'),
    path('leave_history/',leaveHistory,name='leave_history'),
    path('report_generator',reportGenerator,name='report_generator'),
    path('requests_received',requestsReceived,name='requests_received'),
    path('approve/',approve,name='approve'),
    path('reject/',reject,name='reject'),
]
