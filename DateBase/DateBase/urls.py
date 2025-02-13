"""
URL configuration for DateBase project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path ,re_path
from DateBaseApp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',login,name='login'),
    re_path('^Myfiles/$',file_install,name='file_install'),
    re_path('^FilesDispatch/$',file_dispatch,name='file_dispatch'),
    re_path('^NewUser/$',register, name='register'),
    re_path('^AdminForm/$',admin_form, name='admin_form'),
]
