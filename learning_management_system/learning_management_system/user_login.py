from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages

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
    return render(request, 'registration/register.html')
