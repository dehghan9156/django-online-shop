from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from . import views
from .views import ZarinPalPaymentView,ZarinPalVerifyView
app_name="order"

urlpatterns = [
    path("add/product/<int:pk>/",views.AddProductView.as_view(),name="add-product-order"),
    path("show/factor/",views.ShowFactorView.as_view(),name="show-factor"),
    path("delete/product/<int:pk>/",views.DeleteProductFactorView.as_view(),name="delete-product"),
    path("update/factor/<int:pk>/",views.UpdateFactorView.as_view(),name="update-factor"),
    path("payment/<int:pk>/", ZarinPalPaymentView.as_view(), name="payment"),
    path("payment/verify/<int:pk>/", ZarinPalVerifyView.as_view(),name="payment-verify")
]