import django_filters
from django_filters import CharFilter, NumberFilter, ModelChoiceFilter 
from .models import Producto, TipoProducto, Marca
from django import forms


class ProductoFilter(django_filters.FilterSet): 
    producto = CharFilter(field_name='producto', lookup_expr='icontains', label='Nombre producto')
    precio__gte = NumberFilter(field_name='precio', lookup_expr='gte', label='Precio mínimo')
    precio__lte = NumberFilter(field_name='precio', lookup_expr='lte', label='Precio máximo')
    id_tipo_producto = ModelChoiceFilter(empty_label='Todos los tipos', field_name='id_tipo_producto', label='Tipo producto', queryset=TipoProducto.objects.all())
    id_marca = ModelChoiceFilter(empty_label='Todas las marcas', field_name='id_marca', label='Marca', queryset=Marca.objects.all())

    class Meta:
        model = Producto
        fields = ['producto', 'id_tipo_producto', 'id_marca']
