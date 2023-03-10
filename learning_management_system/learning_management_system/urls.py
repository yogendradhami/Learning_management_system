"""learning_management_system URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views,user_login
urlpatterns = [
    path('admin/', admin.site.urls),
    path('base/', views.Base, name='base'),
    path('', views.Home, name= 'home'),
    path('single-cource/', views.SingleCource, name='single-cource'),
    path('contactus/', views.ContactUs, name='contact-us'),
    path('aboutus/', views.AboutUs, name='about-us'),

    path('accounts/register/', user_login.Register, name='register'),
    path('accounts/', include('django.contrib.auth.urls')),
]
