from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="admin_home"),
    path('users', views.users, name="admin_users"),
    path('users/create', views.create_user, name="admin_create_user"),
    path('users/modify/<id>', views.modify_user, name="admin_modify_user"),

]