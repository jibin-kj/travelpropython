from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def login(request):
    if request.method=='POST':
        username1=request.POST['Username']
        password1=request.POST['password']
        user=auth.authenticate(username=username1,password=password1)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"Invalid credentials")
            return redirect('login')

    return render(request,"login.html")
def register(request):
    if request.method=='POST':
        user_name=request.POST['User name']
        firstname = request.POST['First name']
        lastname = request.POST['Last name']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['password1']
        if password==cpassword:
            if User.objects.filter(username=user_name).exists():
                messages.info(request,"username already taken")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"email already taken")
                return redirect('register')
            else:
                user=User.objects.create_user(username=user_name,password=password,first_name=firstname,last_name=lastname,email=email)
                user.save()
                print("user created")
                return redirect('login')

        else:
            messages.info(request,"password not matching")
            print("password not matching")
            return redirect('register')
        return redirect('/')
    return render(request,"register.html")
def logout(request):
    auth.logout(request)
    return redirect('/')