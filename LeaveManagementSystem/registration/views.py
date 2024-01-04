from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.mail import send_mail
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import login as auth_logout
from LeaveManagementSystem.settings import *
from registration.models import *
from leaves.models import *
import json
def home(request):
    # row=Colleges.objects.get(college_name="jntu")
    # print(row.pk)
    # with connection.cursor() as cursor:
    #     cursor.execute("select id from registration_colleges where college_name=%s",params=['jntu'])
    #     s=cursor.fetchone()
    #     print(s[0])
    return render(request,'registration/home.html')
def register(request):
    if request.method=="POST":
        college_name=request.POST['college_name']
        employee_id=request.POST['employee_id']
        # if User.objects.filter(employee_id=employee_id):
        #     messages.error(request,"Given Employee Id already already exists")
        #     return redirect('home')
        username=request.POST['username']
        if User.objects.filter(username=username):
            messages.error(request,"Given Username already exists")
            return redirect('home')
        gender=request.POST['gender']
        phone=request.POST['phone']
        aadhar=request.POST['aadhar']
        email=request.POST['email']
        if User.objects.filter(email=email):
            messages.error(request,"Given Gmail Id already exists")
            return redirect('home')
        department_name=request.POST['department_name']
        section_name=request.POST['section_name']
        designation=request.POST['designation']
        employment_type=request.POST['employment_type']
        employment_status=request.POST['employment_status']
        password=request.POST['password']
        confirm_password=request.POST['confirm_password']
        if password!=confirm_password:
            messages.error(request,"Passwords do not match")
        else:
            current_user=User.objects.create_user(username,email,password)
            current_user.save()
            college_row=Colleges.objects.get(college_name=college_name)
            section_row=Section.objects.get(section_name=section_name)
            dept_row=Department.objects.get(dept_name=department_name)
            if gender=="male" and employment_type=="teaching" and employment_status=="regular":
                leave_balance=json.dumps(male_teaching_regular)
            elif gender=="male" and employment_type=="teaching" and employment_status=="contract":
                leave_balance=json.dumps(male_teaching_contract)
            elif gender=="male" and employment_type=="non teaching" and employment_status=="regular":
                leave_balance=json.dumps(male_non_teaching_regular)
            elif gender=="male" and employment_type=="non teaching" and employment_status=="contract":
                leave_balance=json.dumps(male_non_teaching_contract)
            elif gender=="female" and employment_type=="teaching" and employment_status=="regular":
                leave_balance=json.dumps(female_teaching_regular)
            elif gender=="female" and employment_type=="teaching" and employment_status=="contract":
                leave_balance=json.dumps(female_teaching_contract)
            elif gender=="female" and employment_type=="non teaching" and employment_status=="regular":
                leave_balance=json.dumps(female_non_teaching_regular)
            elif gender=="female" and employment_type=="non teaching" and employment_status=="contract":
                leave_balance=json.dumps(female_non_teaching_contract)
            current_faculty=Faculty(employee_id=employee_id,faculty_name=username,phone=phone,aadhar=aadhar,designation=designation,gender=gender,employment_type=employment_type,employment_status=employment_status,leave_balance=leave_balance,college_id=college_row,dept_id=dept_row,section_id=section_row,user_id=current_user)
            current_faculty.save()
            messages.success(request,"You are successfully registered")
            subject="Welcome Email"
            message="Hi {{ current_user.username }} !\nWe are glad to have you with Jntu Gv Leave Management System"
            from_email=EMAIL_HOST_USER
            receiversList=[current_user.email]
            send_mail(subject=subject,message=message,from_email=from_email,recipient_list=receiversList,fail_silently=True)
            return redirect('login')
    return render(request,'registration/register.html')
def login(request):
    if request.method=="POST":
        employee_id=request.POST['employee_id']
        password=request.POST['password']
        user=authenticate(username=employee_id,password=password)
        if user is not None:
            auth_login(request,user)
            messages.success(request,"You are successfully logged in")
            current_faculty_row=Faculty.objects.get(user_id=user.pk)
            designation=current_faculty_row.designation
            print(designation)
            if designation=="Principal":
                return render(request,'leaves/principal_dashboard.html')
            elif designation=="Department HOD":
                return render(request,'leaves/hod_dashboard.html')
            elif designation=="Employee":
                return render(request,'leaves/employee_dashboard.html')
            else:
                return render(request,'leaves/employee_dashboard.html')
        else:
            messages.error(request,"Not Yet Registered")
            return redirect('home')
    return render(request,'registration/login.html')
def logout(request):
    auth_logout(request)
    messages.success(request,"You are successfully logged out")
    return redirect('home')