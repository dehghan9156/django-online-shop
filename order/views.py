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
import requests

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
        lst = []
        for factor in factors:
            lst.append(factor.total_price)
        total_factor = sum(lst)
        final_factor = total_factor + 52000    
        print(final_factor)
        return render(request,"order/factor.html",{"header_factor":header_factor,"factors":factors,"final_factor":final_factor,"total_factor":total_factor})
    
    
class DeleteProductFactorView(View):
    def post(self,request,pk):
        try:
            header_factor = HeaderFactor.objects.get(user= request.user)
            factor = Factor.objects.get(header_factor=header_factor,pk=pk)
            factor.delete()
            messages.success(request,"your product delete from factor successfully","success")
            return redirect("order:show-factor")
        except Factor.DoesNotExist:
            messages.error(request,"product not found","error")

class UpdateFactorView(View):
    def post(self,request,pk):
        header_factor = HeaderFactor.objects.get(user=request.user)
        factor = Factor.objects.get(header_factor=header_factor,pk=pk)
        quantity = request.POST.get("quantity")
        factor.quantity = quantity
        factor.save()
        messages.success(request,"quantity product updated","success")
        return redirect("order:show-factor")
    

# مقدار مرچنت کد تستی (Sandbox)
MERCHANT = "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
CALLBACK_URL = "http://127.0.0.1:8001/order/payment/verify/"  # آدرس بازگشت بعد از پرداخت

class ZarinPalPaymentView(View):
    def get(self, request, pk):
        """ارسال درخواست پرداخت به زرین‌پال"""
        try:
            header_factor = HeaderFactor.objects.get(pk=pk)
            factors = Factor.objects.filter(header_factor=header_factor)
            lst = []
            for factor in factors:
                lst.append(factor.total_price)
            total_factor = sum(lst)
            final_factor = total_factor + 52000
            amount = int(final_factor)  # مبلغ پرداختی
            print("ok")
            data = {
                "merchant_id": MERCHANT,
                "amount": amount,
                "callback_url": f"{CALLBACK_URL}{pk}/",
                "description": f"پرداخت فاکتور شماره {header_factor.pk}",
            }
            headers = {"Content-Type": "application/json"}

            response = requests.post(
                "https://sandbox.zarinpal.com/pg/v4/payment/request.json",
                json=data,
                headers=headers
            )
            result = response.json()

            if "data" in result and "authority" in result["data"]:
                return redirect(f"https://sandbox.zarinpal.com/pg/StartPay/{result['data']['authority']}")
            else:
                return render(request, "payment/error.html", {"message": result["errors"]["message"]})

        except HeaderFactor.DoesNotExist:
            return render(request, "payment/error.html", {"message": "فاکتور یافت نشد."})

class ZarinPalVerifyView(View):
    def get(self, request,pk):
        header_factor = HeaderFactor.objects.get(pk=pk)
        factors = Factor.objects.filter(header_factor=header_factor)
        lst = []
        for factor in factors:
            lst.append(factor.total_price)
        total_factor = sum(lst)
        final_price = total_factor + 52000
        amount = int(final_price)  # مبلغ پرداختی

        """بررسی وضعیت پرداخت بعد از بازگشت از درگاه"""
        authority = request.GET.get("Authority")
        data = {
            "merchant_id": MERCHANT,
            "amount": amount,
            "authority": authority
        }
        headers = {"Content-Type": "application/json"}

        response = requests.post("https://sandbox.zarinpal.com/pg/v4/payment/verify.json", json=data, headers=headers)
        result = response.json()
        print(result)
        if "data" in result and "code" in result["data"]:
            if result["data"]["code"] == 100:
                header_factor.status = "paid"
                header_factor.save()
                Factor.objects.filter(header_factor=header_factor).delete()
                return render(request, "payment/success.html", {"transId": result["data"]["ref_id"]})
            else:
                return render(request, "payment/error.html", {"message": f"خطای پرداخت: {result['data']} "})
        elif "errors" in result:
            return render(request, "payment/error.html", {"message": f"خطای زرین‌پال: {result['errors']} "})
        else:
            return render(request, "payment/error.html", {"message": "پاسخ نامعتبر از زرین‌پال"})
