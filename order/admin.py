from django.contrib import admin
from django.contrib.admin import ModelAdmin
from .models import * 


class CustomHeaderFactor(ModelAdmin):
    list_display = ("user","status")

class CustomFactor(ModelAdmin):
    list_display =("product","quantity","total_price","header_factor")

admin.site.register(HeaderFactor,CustomHeaderFactor)
admin.site.register(Factor,CustomFactor)