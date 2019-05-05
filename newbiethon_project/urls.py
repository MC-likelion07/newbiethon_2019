"""newbiethon_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
import firstapp.views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', firstapp.views.home, name="home"),
    path('admin/', admin.site.urls),
    path('recom_food/', firstapp.views.recom_food, name="recom_food"),
    path('president/',firstapp.views.president, name='president'),
    path('challenge/', firstapp.views.challenge, name="challenge"),
    path('president/accounts/login/', firstapp.views.login, name='accounts/login'),
    path('president/<int:blog.id>', firstapp.views.login, name=''),
    path('president/accounts/signup/', firstapp.views.signup, name='accounts/signup'),
    path('president/logout/', firstapp.views.logout, name='logout'),
    path('honbob/', firstapp.views.honbob, name='honbob'),
    path('write/', firstapp.views.write, name='write'),
    path('new/',firstapp.views.new, name='new'),
    path('create/',firstapp.views.create, name="create"),
    path('recommend/',firstapp.views.recommend, name="recommend"),
    
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
