from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from . import views


app_name="order"

urlpatterns = [
    path("add/product/<int:pk>/",views.AddProductView.as_view(),name="add-product-order"),

]