from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import datetime

def index(request):
    # 这里将来自数据库的的数据放到一个变量中，然后可以在html中显示
    test_list = ["张","李"]
    context = {'test_list': test_list}
    return render(request, 'web_for_dbwork2/index.html', context)

# 专业
def major_c2m(request):
    return render(request, 'web_for_dbwork2/major_c2m.html')

def major_m2c(request):
    return render(request, 'web_for_dbwork2/major_m2c.html')

def major_recommend(request):
    return render(request, 'web_for_dbwork2/major_recommend.html')

# 学习
def study_main(request):
    return render(request, 'web_for_dbwork2/study_main.html')

def study_router(request):
    return render(request, 'web_for_dbwork2/study_router.html')


# 生活
def life(request):
    return render(request, 'web_for_dbwork2/life.html')

#  测试用
def page1(request):
    text_list = ["hello", "word"]
    contex = {'text_list': text_list}
    return render(request, 'web_for_dbwork2/page1.html', contex)

def page2(request):
    # 获取当前时间
    now = datetime.datetime.now()
    return render(request, 'web_for_dbwork2/page2.html', {"time_now": now})

def login(request):
    # return render(request, 'web_for_dbwork2/login.html')
    return render(request,'users/login.html')
def register(request):
    return render(request,'users/register.html')
    # return render(request, 'web_for_dbwork2/register.html')
