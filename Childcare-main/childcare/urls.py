"""childcare URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path,include
from childapp import views
from event import views

urlpatterns = [
    path('',include('childapp.urls')),
    path('admin/', admin.site.urls),
    path('register/',include('childapp.urls')),
    path('adminpage/',include('childapp.urls')),
    path('event/',include('childapp.urls')),
    path('delete/',include('childapp.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    #path('send_msg_general_events/', include('childapp.urls')),
    #path('accounts/logout/', include('django.contrib.auth.urls')),

]
