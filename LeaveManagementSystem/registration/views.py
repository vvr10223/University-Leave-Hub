from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.mail import send_mail
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import login as auth_logout
from LeaveManagementSystem.settings import *
def home(request):
    return render(request,'registration/home.html')
def register(request):
    if request.method=="POST":
        employee_id=request.POST['employee_id']
        # if User.objects.filter(employee_id=employee_id):
        #     messages.error(request,"Given Employee Id already already exists")
        #     return redirect('home')
        username=request.POST['username']
        if User.objects.filter(username=username):
            messages.error(request,"Given Username already exists")
            return redirect('home')
        phone=request.POST['phone']
        aadhar=request.POST['aadhar']
        email=request.POST['email']
        if User.objects.filter(email=email):
            messages.error(request,"Given Gmail Id already exists")
            return redirect('home')
        department=request.POST['department']
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
            # if user.designation=="Principal":
            #     return render(request,'principal_dashboard')
            # elif user.designation=="HOD":
            #     return render(request,'hod_dashboard')
            # elif user.designation=="Professor" or user.designation=="Office Staff":
            #     return render(request,'employee_dashboard')
            # else:
            #     return render(request,'employee_dashboard')
            return render(request,'leaves/employee_dashboard.html')
        else:
            messages.error(request,"Not Yet Registered")
            return redirect('home')
    return render(request,'registration/login.html')
def logout(request):
    auth_logout(request)
    messages.success(request,"You are successfully logged out")
    return redirect('home')