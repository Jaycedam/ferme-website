import django_filters
from django_filters import CharFilter, NumberFilter, ModelChoiceFilter, ModelMultipleChoiceFilter
from .models import Producto, TipoProducto, Marca, Persona, User
from django import forms

class ProductoFilter(django_filters.FilterSet): 
    producto = CharFilter(field_name='producto', lookup_expr='icontains', label='', widget=forms.TextInput(attrs={'placeholder': 'Buscar'}) )
    precio__gte = NumberFilter(field_name='precio', lookup_expr='gte', label='', widget=forms.TextInput(attrs={'placeholder': 'Precio mayor a', 'type':'number'}))
    precio__lte = NumberFilter(field_name='precio', lookup_expr='lte', label='', widget=forms.TextInput(attrs={'placeholder': 'Precio menor a', 'type':'number'}))
    id_marca = ModelChoiceFilter(field_name='id_marca', label='', queryset=Marca.objects.all(), empty_label='Todas las marcas' )

    class Meta:
        model = Producto
        fields = ['producto', 'id_marca']

class ProductAdminFilter(django_filters.FilterSet): 
    producto = CharFilter(field_name='producto', lookup_expr='icontains', label='Nombre')
    precio__gte = NumberFilter(field_name='precio', lookup_expr='gte', label='Precio mínimo')
    precio__lte = NumberFilter(field_name='precio', lookup_expr='lte', label='Precio máximo')
    id_tipo_producto = ModelChoiceFilter(empty_label='Todos los tipos', field_name='id_tipo_producto', label='Tipo', queryset=TipoProducto.objects.all())
    id_marca = ModelChoiceFilter(empty_label='Todas las marcas', field_name='id_marca', label='Marca', queryset=Marca.objects.all())
    stock__gt = NumberFilter(field_name='stock', lookup_expr='gt', label='Stock mayor a')
    stock__lt = NumberFilter(field_name='stock', lookup_expr='lt', label='Stock menor a')

    class Meta:
        model = Producto
        fields = ['id_producto', 'producto', 'id_tipo_producto', 'id_marca', 'id_proveedor']

class UsuarioAdminFilter(django_filters.FilterSet):
    usuario = CharFilter(field_name='usuario', lookup_expr='icontains', label='Nombre de usuario')
    rut_persona = CharFilter(field_name='rut_persona', lookup_expr='icontains', label='Rut (sin puntos con guión)')
    usuario__first_name = CharFilter(field_name='usuario__first_name', lookup_expr='icontains', label='Nombre')
    usuario__last_name = CharFilter(field_name='usuario__last_name', lookup_expr='icontains', label='Apellido')
    usuario__email = CharFilter(field_name='usuario__email', lookup_expr='icontains', label='Email')
    celular = CharFilter(field_name='celular', lookup_expr='icontains', label='Celular')

    class Meta:
        model = Persona
        fields = ['rut_persona', 'usuario', 'usuario__first_name', 'usuario__last_name', 'celular',  'usuario__email', ]