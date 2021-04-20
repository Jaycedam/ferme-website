from django.urls import path
from .views import inicio, register, admin, perfil, administrador, modificar_perfil

urlpatterns = [
    path('', inicio, name="inicio"),
    path('register/', register, name="register"),
    path('admin/', admin, name="admin"),
    path('administrador/', administrador, name="administrador"),
    path('perfil/', perfil, name="perfil"),
    path('perfil/modificar/', modificar_perfil, name="modificar_perfil"),
]
