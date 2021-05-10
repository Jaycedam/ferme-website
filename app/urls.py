from django.urls import path
from .views import home, register, admin, profile, admin_home, products, product, cart, admin_usuarios, profile_modify, product_management, adress_modify, product_modify

urlpatterns = [
    path('', home, name="home"),
    path('register/', register, name="register"),
    path('admin/', admin, name="admin"),
    path('profile/', profile, name="profile"),
    path('profile/modify', profile_modify, name="profile_modify"),
    path('profile/adress/modify', adress_modify, name="adress_modify"),
    path('products/<id>', products, name="products"),
    path('product/<id>', product, name="product"),
    path('cart', cart, name="cart"),
    path('administrador/home', admin_home, name="admin_home"),
    path('administrador/usuarios', admin_usuarios, name="admin_usuarios"),
    path('employee/product-management', product_management, name="product_management"),
    path('employee/product-modify/<id>', product_modify, name="product_modify"),
]
