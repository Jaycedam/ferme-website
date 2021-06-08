import django_filters
from django_filters import CharFilter, NumberFilter, ModelChoiceFilter, ChoiceFilter
from .models import Persona, User, Marca, FamiliaProducto, TipoProducto
from django import forms

class UsuarioAdminFilter(django_filters.FilterSet):
    persona__rut_persona = CharFilter(label='Rut persona', lookup_expr='icontains', widget=forms.TextInput(attrs={'placeholder': 'Sin puntos con guión'}) )
    email = CharFilter(label='Email', lookup_expr='icontains', widget=forms.TextInput(attrs={'placeholder': '@'}) )
    username = CharFilter(label='Nombre de usuario', lookup_expr='icontains', widget=forms.TextInput(attrs={'placeholder': 'username'}) )
    is_staff = ChoiceFilter(label='Es empleado', choices = {(True,"Sí"),(False,"No")}, empty_label='Seleccionar' )
    is_superuser = ChoiceFilter(label='Es superusuario', choices = {(True,"Sí"),(False,"No")}, empty_label='Seleccionar' )

    class Meta:
        model = User
        fields = ['username', 'email', 'is_staff', 'is_superuser', 'persona__rut_persona']

class BrandAdminFilter(django_filters.FilterSet):
    marca = CharFilter(label='Marca', lookup_expr='icontains', widget=forms.TextInput(attrs={'placeholder': 'Buscar'}) )
    class Meta:
        model = Marca
        fields = ["marca"]

class CategoryFilter(django_filters.FilterSet):
    familia_producto = CharFilter(label='Familia producto', lookup_expr='icontains', widget=forms.TextInput(attrs={'placeholder': 'Buscar'}) )
    class Meta:
        model = FamiliaProducto
        fields = ["familia_producto"]

class SubCategoryFilter(django_filters.FilterSet):
    tipo_producto = CharFilter(label='Familia producto', lookup_expr='icontains', widget=forms.TextInput(attrs={'placeholder': 'Buscar'}) )
    class Meta:
        model = TipoProducto
        fields = ["tipo_producto", "id_familia_producto"]
