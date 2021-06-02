from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="employees_home"),
    # product crud
    path('product-management', views.product_management, name="product_management"),
    path('product-modify/<id>', views.product_modify, name="product_modify"),
    path('product-create', views.product_create, name="product_create"),
    # orders
    path('product-request', views.product_request, name="product_request"),
    path('product-request/<id>', views.products_by_provider, name="products_by_provider"),
    path('order', views.order, name="order"),
    path('order/checkout', views.checkout_provider, name="checkout_provider"),
    # admin
    path('admin-home', views.admin_home, name="admin_home"),
    path('admin-users', views.admin_users, name="admin_users"),

]