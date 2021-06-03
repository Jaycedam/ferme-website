import django_filters
from django_filters import CharFilter, NumberFilter, ModelChoiceFilter
from .models import Producto, TipoProducto, Marca, Persona, User, FamiliaProducto, Proveedor
from django import forms

class ProductAdminFilter(django_filters.FilterSet): 
    id_producto = CharFilter(field_name='id_producto', lookup_expr='icontains', label='ID producto', widget=forms.TextInput(attrs={'placeholder': 'Buscar'}))
    producto = CharFilter(field_name='producto', lookup_expr='icontains', label='Nombre producto', widget=forms.TextInput(attrs={'placeholder': 'Buscar'}))
    id_tipo_producto__id_familia_producto = ModelChoiceFilter(empty_label='Seleccionar', field_name='id_tipo_producto__id_familia_producto', label='Familia producto', queryset=FamiliaProducto.objects.all())
    id_marca = ModelChoiceFilter(empty_label='Seleccionar', field_name='id_marca', label='Marca', queryset=Marca.objects.all())
    stock__lt = NumberFilter(field_name='stock', lookup_expr='lt', label='Stock menor a', widget=forms.TextInput(attrs={'placeholder': 'Buscar', 'type':'number'}))
    id_proveedor = ModelChoiceFilter(empty_label='Seleccionar', field_name='id_proveedor', label='Proveedor', queryset=Proveedor.objects.all())

    class Meta:
        model = Producto
        fields = ['id_producto' ,'producto', 'id_marca', 'id_tipo_producto__id_familia_producto', 'id_proveedor']