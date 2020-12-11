
from django.shortcuts import render

from django.shortcuts import render
# Create your views here.
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.urls import reverse

from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm

def logout(request):
    # logout(request)
    # return HttpResponseRedirect(reverse('web_for_dbwork2:index'))
    return render(request, 'web_for_dbwork2/index.html')


def login(request):
    return render(request, 'users/login.html')

def register(request):
    return render(request, 'users/register.html')

    # if request.method != 'POST':
    #     # Display blank registration form.
    #     form = UserCreationForm()
    # else:
    #     # Process completed form.
    #     form = UserCreationForm(data=request.POST)
    #
    #     if form.is_valid():
    #         new_user = form.save()
    #         # Log the user in, and then redirect to home page.
    #         authenticated_user = authenticate(username=new_user.username,
    #                                           password=request.POST['password1'])
    #         login(request, authenticated_user)
    #         return HttpResponseRedirect(reverse('web_for_dbwork2:index'))
    #
    # context = {'form': form}
    # return render(request, 'users/register.html', context)