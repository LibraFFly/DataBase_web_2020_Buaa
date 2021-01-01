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

app_name = "web_for_dbwork2"

urlpatterns = [
    path('index/', views.index, name='index'),

    #  专业
    path('major_c2m/', views.major_c2m, name='major_c2m'),
    path('major_m2c/', views.major_m2c, name='major_m2c'),
    path('.major_recommend/', views.major_recommend, name='major_recommend'),
    # 学习
    path('study_main/', views.study_main, name='study_main'),
    path('study_router/', views.study_router, name='study_router'),
    # 生活
    path('life/', views.life, name='life'),


    # 专业推荐发帖
    path('add_major_recommend/', views.add_major_recommend, name='add_major_recommend'),

    # 生活发帖
    path('add_life_topic/', views.add_life_topic, name='add_life_topic'),

    # 学习路线发帖
    path('add_study_router/', views.add_study_router, name='add_study_router'),

    path('add_xing/', views.add_xing, name='add_xing'),
    path('add_grade/', views.add_grade, name='add_grade'),
    path('add_life/', views.add_life, name='add_life'),
    # 测试用
    path('page1/', views.page1, name='page1_name'),
    path('page2/', views.page2, name='page2_name'),

]