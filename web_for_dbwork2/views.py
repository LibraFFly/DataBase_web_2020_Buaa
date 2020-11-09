from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the  index.")

def page1(request):
    return HttpResponse("zwhnb!")

def page2(request):
    return HttpResponse("zwhnbnb!!!")