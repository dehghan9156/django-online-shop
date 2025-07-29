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
        factor = Factor.objects.filter(header_factor=header_factor,product=product).first()
        if not factor:
            Factor.objects.create(header_factor=header_factor,product=product,quantity=1)
        else:
            factor.quantity += 1
            factor.save()

        messages.success(request,"product add successfully","success")
        return redirect("product:detail-product",pk=pk)
    
class ShowFactorView(View):
    def get(self,request):
        header_factor = HeaderFactor.objects.get(user=request.user)
        factors = Factor.objects.filter(header_factor=header_factor)
        return render(request,"order/factor.html",{"header_factor":header_factor,"factors":factors})