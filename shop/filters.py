import django_filters
from django_filters import CharFilter, NumberFilter, ModelChoiceFilter
from .models import Producto, Marca
from django import forms

class ProductoFilter(django_filters.FilterSet): 
    producto = CharFilter(field_name='producto', lookup_expr='icontains', label='', widget=forms.TextInput(attrs={'placeholder': 'Buscar'}) )
    precio__gte = NumberFilter(field_name='precio', lookup_expr='gte', label='', widget=forms.TextInput(attrs={'placeholder': 'Precio mayor a', 'type':'number'}))
    precio__lte = NumberFilter(field_name='precio', lookup_expr='lte', label='', widget=forms.TextInput(attrs={'placeholder': 'Precio menor a', 'type':'number'}))
    id_marca = ModelChoiceFilter(field_name='id_marca', label='', queryset=Marca.objects.all(), empty_label='Todas las marcas' )

    class Meta:
        model = Producto
        fields = ['producto', 'id_marca']