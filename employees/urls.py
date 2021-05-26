from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="employees_home"),
    path('product-management', views.product_management, name="product_management"),
    path('product-request', views.product_request, name="product_request"),
    path('product-request/<id>', views.products_by_provider, name="products_by_provider"),
    path('order', views.order, name="order"),
    path('order/checkout', views.checkout_provider, name="checkout_provider"),
    path('product-modify/<id>', views.product_modify, name="product_modify"),
]