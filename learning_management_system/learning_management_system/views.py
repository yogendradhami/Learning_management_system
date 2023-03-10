from django.shortcuts import redirect, render

def Base(request):
    return render(request, 'base.html')

def Home(request):
    return render(request, 'main/home.html')
