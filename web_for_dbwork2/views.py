from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    # 这里将来自数据库的的数据放到一个变量中，然后可以在html中显示
    test_list = ["张","李"]
    context = {'test_list': test_list}
    return render(request, 'web_for_dbwork2/index.html', context)

def page1(request):
    return HttpResponse("zwhnb!")

def page2(request):
    return HttpResponse("zwhnbnb!3!!")