"""
URL configuration for dj1_project project.

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
    
将url路径与python函数对应起来
"""
from django.contrib import admin
from django.urls import path

from app01 import views 

urlpatterns = [
    #path('admin/', admin.site.urls),
    #www.xxx.com/index/ -> admin.site.urls
    path('index/', views.index),
    path('index_niubi/', views.index_niubi),
    path('user_list/', views.user_list),
    path('tpl/', views.template_test),
    path('tpl2/', views.template_test2),
    path("weiliantong/",views.weiliantongji),
    #请求和相应
    path('something/',views.request_something),
    #用户登录
    path('login/',views.login),
    path('orm/',views.orm),
    #用户管理
    path('info/list/',views.user_list),
    #添加用户
    path('info/add/',views.user_add),
    #删除用户
    path('info/del/',views.user_del)
]
