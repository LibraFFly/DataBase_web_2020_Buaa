# -*- coding: utf-8 -*-

'''
@Time    : 2020/11/9 23:32
@Author  : Wanhao Zhang
@Contact : 1809721229@qq.com 
@FileName: urls.py
@Software: PyCharm
 
'''
from django.urls import path

from web_for_dbwork2 import views

app_name="web_for_dbwork2"

urlpatterns = [
    path('index/', views.index, name='index'),
    path('page1/', views.page1, name='page1_name'),
    path('page2/', views.page2, name='page2_name'),
    path('major/', views.major, name='major'),
    path('login/', views.login, name="login"),
    path('register/',views.register, name="register"),
    path('route_query/', views.route_query, name="route_query"),
]