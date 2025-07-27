from django.shortcuts import render
from django.contrib.messages import success
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponse
from .forms import *
from django.contrib.auth import authenticate,login,logout




class RegisterUserView(View):
    print("test view")
    def get(self,request):
        form = UserRegisterForm()
        return render(request,"accounts/user-register.html",{"form":form})
    
    def post(self,request):
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = User.objects.create_user(email=cd['email'],password=cd['password'])
            user.save()
            return HttpResponse("ok")
        return render(request,"accounts/user-register.html",{"form":form})

class LoginUserView(View):
    def get(self,request):
        form = UserLoginForm
        return render(request,"accounts/user-login.html",{"form":form}) 
    
    def post(self,request):
        print("cd")
        form = UserLoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,username=cd["email"], password=cd["password"])
            if user is not None :
                login(request, user)
                return redirect("/")
            messages.error(request,"user with this email is not found","error")
        else:
            messages.error(request,"email or password is not correct","error")

        return render(request,"accounts/user-login.html",{"form":form})

class LogoutUserView(View):
    def get(self,request):
        logout(request)
        messages.success(request,"user logout successfully.","success")
        return redirect("accounts:login-user")