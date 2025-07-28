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
from .forms import *
from django.urls import reverse_lazy,reverse

class HomeView(View):
    def get(self,request):
        products = Product.objects.all()
        return render(request,"product/home.html",{"products":products})

class DetailProductView(View):
    def get(self,request,pk):
        product = Product.objects.get(pk=pk)
        return render(request,"product/detail.html",{"product":product})

class EditProductView(UpdateView):
    form_class = ProductCreateUpdateForm
    model = Product
    template_name = "product/update.html"

    def get_success_url(self):
        return reverse("product:detail", kwargs={"pk": self.object.pk})

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_staff:
            messages.error(request, 'You cannot edit product', 'error')
            return redirect("product:product-list")
        return super().dispatch(request, *args, **kwargs)

class DeleteProductView(DeleteView):
    model = Product
    template_name = "product/delete.html"
    success_url = reverse_lazy("product:home")

    def delete(self, request, *args, **kwargs):
        messages.success(request, "Product deleted successfully.","success")
        return super().delete(request, *args, **kwargs)

class AddProductView(View):
    def get(self,request):
        form = ProductCreateUpdateForm()
        return render(request,"product/add.html",{"form":form})
    def post(self,request):
        form = ProductCreateUpdateForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"your product add successfully.","success")
            return redirect("product:home")
        else:
            messages.error(request,"form is not valid.","error")
        
        return render(request,"product/add.html",{"form":form})
