from django.contrib import messages
from django.shortcuts import render, redirect

from django.shortcuts import render
# Create your views here.
from django.contrib.auth import logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse

from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm

from users.models import All_Users
from web_db.base import check_login
from web_for_dbwork2.models import User_Info, Focus_Record, Broadcast_Record, Favorite_Record


def logout(request):
    # logout(request)
    # return HttpResponseRedirect(reverse('web_for_dbwork2:index'))
    request.COOKIES.clear()
    request.session.clear()
    response = redirect("users:login")
    response.set_cookie("IS_LOGIN", None)
    response.delete_cookie("IS_LOGIN")
    return response


def register(request):
    if request.method == "POST":
        """Register a new user."""
        register_name = request.POST.get("register_name")
        grade = request.POST.get("grade")
        major = request.POST.get("major")

        register_mail = request.POST.get("register_mail")
        register_password = request.POST.get("register_password")
        again_password = request.POST.get("again_password")
        if register_password != again_password:
            messages.error(request, "两次密码不一致，请重试")
            return HttpResponseRedirect(reverse('users:register'))
        # print(register_name, register_password, register_mail)
        user = All_Users(user_name=register_name, user_email=register_mail, user_password=register_password)
        user.save()

        id = All_Users.objects.last()
        ins = User_Info(user_id=id.user_id, user_grade=grade, user_major=major, user_grant=2)
        ins.save()

        # 重定向到登陆界面
        messages.success(request, "注册成功，恭喜您成为航亦有道大会员！")
        return redirect("users:login")
    """jump to html"""
    # url链接该视图，定向到注册页面
    return render(request, "users/register.html")


def login(request):
    if request.method == "POST":
        login_name = request.POST.get("login_name")
        login_password = request.POST.get("login_password")
        exist_name = All_Users.objects.filter(user_name=login_name)
        user = All_Users.objects.filter(user_name=login_name, user_password=login_password)

        # print(login_name, login_password)
        # print(len(user), len(exist_name))

        if len(user) >= 1:
            # 存下当前登陆进来的用户
            response = redirect(reverse("web_for_dbwork2:index"))
            response.set_cookie("user_id", user[0].user_id)
            response.set_cookie("user_name", user[0].user_name)
            response.set_cookie("user_email", user[0].user_email)
            # 标识用户已经登录，用于页面访问权限
            response.set_cookie("IS_LOGIN", True)
            # 用户名传出去
            request.session['login_name'] = login_name
            request.session['is_authenticated'] = True

            messages.success(request, "登陆成功，欢迎相约航亦有道！")

            return response

        elif len(exist_name) == 1 and len(user) == 0:
            messages.error(request, "粗心啦，密码不对噢")
            return redirect("users:login")
        else:
            messages.error(request, "找不到此用户呢，您可能没有注册噢")
            return redirect("users:login")

    return render(request, "users/login.html")


@check_login
def person_informarion(request):
    res = {}

    user_id = request.COOKIES.get("user_id")
    user_info = User_Info.objects.filter(user_id=user_id)
    grade = user_info[0].user_grade
    major = user_info[0].user_major
    res['grade'] = grade
    res['major'] = major
    res['name'] = request.COOKIES.get("user_name")

    # 取用户关注记录
    focus_info_list = Focus_Record.objects.filter(user_id=user_id).values("focus_id", "focus_time")

    focus_info = []

    for info in focus_info_list:
        name = All_Users.objects.filter(user_id=info['focus_id'])[0].user_name
        focus_info.append({'focus_name': name, 'focus_time': info['focus_time']})

    res['focus_info_list'] = focus_info

    # 取用户发布记录
    broadcast_list = []

    broadcast_record = Broadcast_Record.objects.filter(user_id=user_id)

    for record in broadcast_record:
        title = record.title
        time = record.broadcast_time
        broadcast_list.append({'broadcast_time': time, 'title': title})

    res['broadcast_list'] = broadcast_list

    # 取用户收藏记录
    # 学习路线
    study = []
    # 生活
    lives = []
    # 专业推荐帖子
    major = []

    favorite_info = Favorite_Record.objects.filter(user_id=user_id)
    for info in favorite_info:
        title = info.favorite_title
        owner_name = info.owner_name
        time = info.favorite_time
        contentAndId = info.favorite_content_id
        if contentAndId[0:5] == "study":
            study.append({'title': title, 'owner_name': owner_name, 'time': time})
            pass
        elif contentAndId[0:5] == "lives":
            lives.append({'title': title, 'owner_name': owner_name, 'time': time})
            pass
        elif contentAndId[0:5] == "major":
            major.append({'title': title, 'owner_name': owner_name, 'time': time})
            pass
        else:
            pass

    res['fav_study'] = study
    res['fav_lives'] = lives
    res['fav_major'] = major

    return render(request, 'users/person_information.html', res)


def deleteUser(request):
    user_id = request.COOKIES["user_id"]
    All_Users.objects.filter(user_id=user_id).delete()
    User_Info.objects.filter(user_id=user_id).delete()
    request.COOKIES.clear()
    request.session.clear()
    response = redirect("users:login")
    response.set_cookie("IS_LOGIN", None)
    response.delete_cookie("IS_LOGIN")
    return response
