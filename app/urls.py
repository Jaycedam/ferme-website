from django.urls import path
from .views import home, register, admin, profile

urlpatterns = [
    path('', home, name="home"),
    path('register/', register, name="register"),
    path('admin/', admin, name="admin"),
    path('profile/', profile, name="profile"),
]
