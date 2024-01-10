from django.shortcuts import render,redirect
from registration.models import *
from leaves.models import *
import json
from datetime import datetime
from django.contrib import messages
from django.utils import timezone
from django.http import HttpResponse

def leaveApplication(request):
    current_faculty=Faculty.objects.get(user_id=request.user.pk)
    current_dept=Department.objects.get(pk=current_faculty.dept_id.pk)
    if request.method=='POST':
        year=timezone.now().year
        employee_id=current_faculty
        dept_id=current_dept
        start_date_str = request.POST.get('start_date')
        end_date_str = request.POST.get('end_date')
        start_date = datetime.strptime(start_date_str, '%Y-%m-%d')
        end_date = datetime.strptime(end_date_str, '%Y-%m-%d')
        date_difference=end_date-start_date
        number_of_days=date_difference.days+1
        leave_type=request.POST['leave_type']
        reason=request.POST['reason']
        if current_faculty.designation=="HOD":
            status=json.dumps(status_hod_accepted)
        elif current_faculty.designation=="Principal":
            status=json.dumps(principal_status_default)
        elif current_faculty.designation=="Registrar":
            status=json.dumps(registrar_status_default)
        else:
            status=json.dumps(status_default)
        current_leave=Leaves(year=year,employee_id=employee_id,dept_id=dept_id,start_date=start_date,end_date=end_date,number_of_days=number_of_days,leave_type=leave_type,reason=reason,status=status)
        current_leave.save()
        messages.success(request,"Leave applied successfully")
    remaining_leaves=json.loads(current_faculty.leave_balance)
    params={"faculty" : current_faculty,"remaining_leaves" : remaining_leaves}
    return render(request,'leaves/leave_application.html',params)
def leaveHistory(request):
    current_faculty=Faculty.objects.get(user_id=request.user.pk)
    user_leaves=Leaves.objects.filter(employee_id=current_faculty.employee_id).order_by('-applied_date')
    params={"current_user_leaves" : user_leaves,"faculty" : current_faculty}
    return render(request,'leaves/leave_history.html',params)
def reportGenerator(request):
    current_faculty=Faculty.objects.get(user_id=request.user.pk)
    params={"faculty" : current_faculty}
    return render(request,'leaves/report_generator.html',params)
def requestsReceived(request):
    current_faculty=Faculty.objects.get(user_id=request.user.pk)
    if current_faculty.designation=="HOD":
        leaves_to_approve=Leaves.objects.filter(dept_id=current_faculty.dept_id.pk,status=json.dumps(status_default))
    elif current_faculty.designation=="Principal":
        leaves_to_approve=Leaves.objects.filter(status=json.dumps(status_hod_accepted))
    elif current_faculty.designation=="Registrar":
        leaves_to_approve=Leaves.objects.filter(status=json.dumps(principal_status_default))
    elif current_faculty.designation=="Vice Chancellor":
        leaves_to_approve=Leaves.objects.filter(status=json.dumps(registrar_status_default))
    params={"faculty" : current_faculty,"leaves_to_approve" : leaves_to_approve}
    return render(request,'leaves/requests_received.html',params)
def approve(request):
    val=request.GET.get('value_to_send')
    approved_leave=Leaves.objects.get(pk=val)
    leave_type=approved_leave.leave_type
    current_faculty=Faculty.objects.get(user_id=request.user.pk)
    if current_faculty.designation=="HOD":
        approved_leave.status=json.dumps(status_hod_accepted)
    elif current_faculty.designation=="Principal":
        approved_leave.status=json.dumps(status_accepted)
    elif current_faculty.designation=="Registrar":
        approved_leave.status=json.dumps(principal_status_registrar_accepted)
    elif current_faculty.designation=="Vice Chancellor":
        approved_leave.status=json.dumps(registrar_status_viceChancellor_accepted)
    approved_leave.save()
    leave_faculty=Faculty.objects.get(pk=approved_leave.employee_id.employee_id)
    leave_balance=json.loads(leave_faculty.leave_balance)
    if "variable" in leave_balance.keys():
         leave_balance["variable"][leave_type]-=1
    else:
        leave_balance[leave_type]-=1
    current_faculty.leave_balance=json.dumps(leave_balance)
    current_faculty.save()
    print(current_faculty.leave_balance)
    messages.success(request,"Leave successfully approved")
    return redirect('requests_received')
def reject(request):
    val=request.GET.get('value_to_send')
    approved_leave=Leaves.objects.get(pk=val)
    current_faculty=Faculty.objects.get(user_id=request.user.pk)
    if current_faculty.designation=="HOD":
        approved_leave.status=json.dumps(status_rejected)
    elif current_faculty.designation=="Principal":
        approved_leave.status=json.dumps(status_rejected)
    elif current_faculty.designation=="Registrar":
        approved_leave.status=json.dumps(principal_status_registrar_rejected)
    elif current_faculty.designation=="Vice Chancellor":
        approved_leave.status=json.dumps(registrar_status_viceChancellor_rejected)
    approved_leave.save()
    messages.success(request,"Leave Rejected Successfully")
    return redirect('requests_received')