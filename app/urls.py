from django.urls import path
from .views import inicio, register, admin, perfil, admin_home, modificar_perfil, productos, producto, cart, admin_productos, admin_usuarios

urlpatterns = [
    path('', inicio, name="inicio"),
    path('register/', register, name="register"),
    path('admin/', admin, name="admin"),
    path('perfil/', perfil, name="perfil"),
    path('perfil/modificar/', modificar_perfil, name="modificar_perfil"),
    path('productos/<id>', productos, name="productos"),
    path('producto/<id>', producto, name="producto"),
    path('cart', cart, name="cart"),
    path('administrador/home', admin_home, name="admin_home"),
    path('administrador/productos', admin_productos, name="admin_productos"),
    path('administrador/usuarios', admin_usuarios, name="admin_usuarios"),


]
