from django.urls import path
from . import views

urlpatterns = [
    path('', views.orders, name="orders"),
    path('order<id>', views.order, name="order"),
]