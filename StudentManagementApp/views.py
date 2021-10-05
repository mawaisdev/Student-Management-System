from django.contrib.auth import login, logout
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
# Create your views here.
from StudentManagementApp import EmailBackend


def showDemoPage(request):
    return render(request, "index.html")


def login_user(request):
    return render(request, "login.html")


def dologin(request):
    if request.method != "POST":
        return HttpResponse("<h2>Method Not allowed</h2>")
    else:
        user = EmailBackend.EmailBackEnd.authenticate(request, username=request.POST.get("email"),
                                                      password=request.POST.get("password"))
        if user is not None:
            login(request, user)
            if user.user_type == "1":
                return HttpResponseRedirect("/admin_home")
            elif user.user_type == "2":
                return HttpResponse("Staff Login")
            else:
                return HttpResponse("Student login")
        else:
            messages.error(request, "Invalid Credentials")
            return HttpResponseRedirect("/")


def GetUserDetails(request):
    if request.user is not None:
        return HttpResponse("User: "+request.user.email+"</br>User Type: " + request.user.user_type)
    else:
        return HttpResponse("<h2>Please Login First. </h2>")


def logout_user(request):
    logout(request)
    return HttpResponseRedirect("/")
