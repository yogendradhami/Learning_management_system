from django.shortcuts import redirect, render

def Register(request):
    return render(request, 'registration/register.html')
