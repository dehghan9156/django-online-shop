from django.contrib import admin
from django.urls import path,include
from . import views



app_name = "product"

urlpatterns = [
    path("",views.HomeView.as_view(),name="home"),
    path("detail/<int:pk>/",views.DetailView.as_view(),name="detail"),
    path("edit/<int:pk>/",views.EditView.as_view(),name="edit"),
    
]