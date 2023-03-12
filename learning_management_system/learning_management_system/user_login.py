from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from app_lms.EmailBackEnd import EmailBackEnd
from django.contrib.auth import authenticate,login,logout

def Register(request):
    if request.method == 'POST':
        username= request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        # email validation
        if User.objects.filter(email=email).exists():
            messages.warning(request, 'Email are already Exists !')
            return redirect('register')
        
        # check username
        if User.objects.filter(username=username).exists():
            messages.warning(request,'Username are Already exists !')
            return redirect('register')
        
        # check password
        if User.objects.filter(password=password).exists():
            messages.warning(request, 'Password is already Exists !')
            return redirect('register')
        
        user =User(username=username, email=email,)
        user.set_password(password)
        user.save()
        messages.success(request, 'Your account has been created successfully !')
        return redirect('login')
    return render(request, 'registration/register.html')


def Login(request):
    if request.method =='POST':
        email=request.POST.get('email')
        password = request.POST.get('password')

        user= EmailBackEnd.authenticate(request,username=email, password=password)

        if user != None:
            login(request,user)
            messages.success('You are Logged In !')
            return redirect('home')
        
        else:
            messages.error(request, 'Email and Password Are invalid')
            return redirect('login')

 