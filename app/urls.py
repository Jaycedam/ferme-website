from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('register/', views.register, name="register"),
    path('admin/', views.admin, name="admin"),
    path('profile/', views.profile, name="profile"),
    path('profile/order/<id>', views.order_details, name="order_details"),
    path('profile/modify', views.profile_modify, name="profile_modify"),
    path('profile/adress/modify', views.adress_modify, name="adress_modify"),
    path('products/<id>', views.products, name="products"),
    path('product/<id>', views.product, name="product"),
    path('cart', views.cart, name="cart"),
    path('cart/checkout', views.checkout, name="checkout"),
    path('employee/product-management', views.product_management, name="product_management"),
    path('employee/product-request', views.product_request, name="product_request"),
    path('employee/product-request/<id>', views.products_by_provider, name="products_by_provider"),
    path('employee/order', views.order, name="order"),
    path('employee/order/checkout', views.checkout_provider, name="checkout_provider"),
    path('employee/product-modify/<id>', views.product_modify, name="product_modify"),
]