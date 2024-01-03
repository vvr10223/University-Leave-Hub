from django.shortcuts import render

def principal_dashboard(request):
    return render(request,'leaves/principal_dashboard.html')
def hod_dashboard(request):
    return render(request,'leaves/hod_dashboard.html')
def employee_dashboard(request):
    return render(request,'leaves/employee_dashboard.html')
