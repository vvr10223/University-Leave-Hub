from django.shortcuts import render
from registration.models import Faculty
from leaves.models import *
import json
from datetime import datetime,timedelta


def leaveApplication(request):
    current_faculty=Faculty.objects.get(user_id=request.user.pk)
    if request.method=='POST':
        employee_id=current_faculty
        start_date_str = request.POST.get('start_date')
        end_date_str = request.POST.get('end_date')
        start_date = datetime.strptime(start_date_str, '%Y-%m-%d')
        end_date = datetime.strptime(end_date_str, '%Y-%m-%d')
        date_difference=end_date-start_date
        number_of_days=date_difference.days+1
        leave_type=request.POST['leave_type']
        reason=request.POST['reason']
        status=json.dumps(status_default)
        current_leave=Leaves(employee_id=employee_id,start_date=start_date,end_date=end_date,number_of_days=number_of_days,leave_type=leave_type,reason=reason,status=status)
        current_leave.save()
    remaining_leaves=json.loads(current_faculty.leave_balance)
    params={"faculty" : current_faculty,"remaining_leaves" : remaining_leaves}
    return render(request,'leaves/leave_application.html',params)
def leaveHistory(request):
    current_faculty=Faculty.objects.get(user_id=request.user.pk)
    params={"faculty" : current_faculty}
    return render(request,'leaves/leave_history.html',params)
def reportGenerator(request):
    current_faculty=Faculty.objects.get(user_id=request.user.pk)
    params={"faculty" : current_faculty}
    return render(request,'leaves/report_generator.html',params)
def requestsReceived(request):
    current_faculty=Faculty.objects.get(user_id=request.user.pk)
    params={"faculty" : current_faculty}
    return render(request,'leaves/requests_received.html',params)
