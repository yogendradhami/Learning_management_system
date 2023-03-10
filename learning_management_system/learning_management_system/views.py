from django.shortcuts import redirect, render

def Base(request):
    return render(request, 'base.html')

def Home(request):
    return render(request, 'main/home.html')

def SingleCource(request):
    return render(request, 'main/single_cource.html')

def ContactUs(request):
    return render(request, 'main/contact_us.html')

def AboutUs(request):
    return render(request, 'main/about_us.html'),
