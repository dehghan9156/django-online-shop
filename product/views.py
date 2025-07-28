from django.shortcuts import render
from django.contrib.messages import success
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from .models import *

class HomeView(View):
    def get(self,request):
        products = Product.objects.all()
        return render(request,"product/home.html",{"products":products})

class DetailView(View):
    def get(self,request,pk):
        product = Product.objects.get(pk=pk)
        return render(request,"product/detail.html",{"product":product})