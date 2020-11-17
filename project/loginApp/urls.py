from django.urls import path, re_path
from . import views

urlpatterns = [
    re_path("loginPage", views.init),
    re_path("loginCheck", views.login),

]
