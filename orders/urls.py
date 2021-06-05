from django.urls import path
from . import views
from . import utils

urlpatterns = [
    path('', views.orders, name="orders"),
    path('order/<id>', views.order, name="order"),
    path('orders-provider', views.orders_to_provider, name="orders_to_provider"),
    path('order-provider/<id>', views.order_provider, name="order_provider"),
    path('order-requests', views.order_requests, name="order_requests"),
    path('order-requests/<id>', views.order_request, name="order_request"),
    path('render_pdf/<id>', utils.render_pdf, name="render_pdf"),
]