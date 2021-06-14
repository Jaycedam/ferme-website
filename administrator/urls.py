from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="admin_home"),
    # usuarios crud
    path('users', views.users, name="admin_users"),
    path('users/create', views.create_user, name="admin_create_user"),
    path('users/modify/<id>', views.modify_user, name="admin_modify_user"),
    # marca crud
    path('brands', views.brands, name="brands"),
    path('brands/create', views.brand_create, name="brand_create"),
    path('brands/modify/<id>', views.brand_modify, name="brand_modify"),
    # familia producto crud
    path('categories', views.categories, name="categories"),
    path('categories/create', views.category_create, name="category_create"),
    path('categories/modify/<id>', views.category_modify, name="category_modify"),
    # tipo producto crud
    path('subcategories', views.subcategories, name="subcategories"),
    path('subcategories/create', views.subcategory_create, name="subcategory_create"),
    path('subcategories/modify/<id>', views.subcategory_modify, name="subcategory_modify"),
    # rubros proveedor crud
    path('areas', views.areas, name="areas"),
    path('areas/create', views.area_create, name="area_create"),
    path('areas/modify/<id>', views.area_modify, name="area_modify"),
    # motivos cancelacion crud
    path('motives', views.motives, name="motives"),
    path('motives/create', views.motive_create, name="motive_create"),
    path('motives/modify/<id>', views.motive_modify, name="motive_modify"),
]