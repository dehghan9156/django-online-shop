from django.contrib import admin
from django.urls import path,include
from . import views



app_name = "product"

urlpatterns = [
    path("",views.HomeView.as_view(),name="home"),
    path("detail/<int:pk>/",views.DetailProductView.as_view(),name="detail-product"),
    path("edit/<int:pk>/",views.EditProductView.as_view(),name="edit-product"),
    path("delete/<int:pk>/",views.DeleteProductView.as_view(),name="delete-product"),
    path("add/",views.AddProductView.as_view(),name="add-product")
    
]