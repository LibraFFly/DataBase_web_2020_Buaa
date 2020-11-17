from django.shortcuts import render


# Create your views here.
def init(request):
    return render(request, "login.html")


def login(request):
    show_content = {}
    login_name = request.POST.get("login_name")
    password = request.POST.get("password")
    show_content['login_name'] = login_name
    return render(request, "main.html", show_content)
