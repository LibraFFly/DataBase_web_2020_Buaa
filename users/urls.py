# -*- coding: utf-8 -*-

'''
@Time    : 2020/11/21 16:11
@Author  : Wanhao Zhang
@Contact : 1809721229@qq.com 
@FileName: urls.py
@Software: PyCharm
 
'''
# from django.conf.urls import url
# from django.contrib.auth.views import auth_login
#
# from . import views
#
# app_name='users'
# urlpatterns = [
#     # 登录页面
#     url(r'^login/$',auth_login, {'template_name': 'users/login.html'}, name='login'),
# ]
from django.conf.urls import url
from django.contrib.auth.views import LoginView
from . import views

app_name = 'users'

urlpatterns = [
    # 登录页面
    # url(r'^login/$', login, {'template_name': 'users/login.html'}, name = 'login'),
    url(r'^login/$', views.login, name="login"),
    url(r"^logout/$", views.logout, name='logout'),
    url(r'^register/$', views.register, name='register'),
    url(r'^person_information/$', views.person_informarion, name='person_information'),
    url(r'^deleteUser/$', views.deleteUser, name="deleteUser"),
]