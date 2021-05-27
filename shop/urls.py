from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('register/', views.register, name="register"),
    path('admin/', views.admin, name="admin"),
    path('profile/', views.profile, name="profile"),
    path('profile/modify', views.profile_modify, name="profile_modify"),
    path('profile/adress/modify', views.adress_modify, name="adress_modify"),
    path('products/<id>', views.products, name="products"),
    path('product/<id>', views.product, name="product"),
    path('cart', views.cart, name="cart"),
    path('cart/checkout', views.checkout, name="checkout"),
]