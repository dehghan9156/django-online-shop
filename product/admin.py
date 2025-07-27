from django.contrib import admin
from .models import *
from django.contrib.admin import ModelAdmin


class CustomProduct(ModelAdmin):
    list_display=("name","price","quantity","discount")




admin.site.register(Category)
admin.site.register(Product,CustomProduct)