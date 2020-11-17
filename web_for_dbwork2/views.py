from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import datetime

def index(request):
    # 这里将来自数据库的的数据放到一个变量中，然后可以在html中显示
    test_list = ["张","李"]
    context = {'test_list': test_list}
    return render(request, 'web_for_dbwork2/index.html', context)

def page1(request):
    text_list = ["hello", "word"]
    contex = {'text_list': text_list}
    return render(request, 'web_for_dbwork2/page1.html', contex)

def page2(request):
    # 获取当前时间
    now = datetime.datetime.now()
    return render(request, 'web_for_dbwork2/page2.html', {"time_now": now})