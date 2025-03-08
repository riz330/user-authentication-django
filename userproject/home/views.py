from imaplib import _Authenticator
from django.shortcuts import render
# from flask import redirect
from requests import request
from django.contrib.auth.models import  User
from django.contrib.auth import authenticate,logout,login

from django.shortcuts import redirect
# Create your views here.


def index(request):
    if request.user.is_anonymous:
        return redirect('/login')
    return render(request,'index.html')

def loginUser(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        # print(username,password)
        # check if he has correct credentials
        user= authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect("/")
            # A Backend Authenticated The Credentials
        else:
            # No Backend Authentication 
            return render(request,'login.html')

    return render(request,'login.html')

def logoutuser(request):
    logout(request)
    return redirect("/login")

# def index(request):
#     return(request,'index.html')
