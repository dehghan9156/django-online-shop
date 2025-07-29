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
from django.urls import reverse_lazy,reverse
from product.models import *
from .models import * 


class AddProductView(LoginRequiredMixin,View):
    def post(self,request,pk):
        product = get_object_or_404(Product,pk=pk)
        header_factor,created = HeaderFactor.objects.get_or_create(user=request.user)
        factor = Factor.objects.create(product=product,header_factor=header_factor)
        messages.success(request,"product add successfully","success")
        return redirect("product:detail-product",pk=pk)
    