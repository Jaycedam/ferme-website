import django_filters
from django_filters import CharFilter, NumberFilter, ModelChoiceFilter
from .models import Producto, Marca
from django import forms

class ProductoFilter(django_filters.FilterSet): 
    producto = CharFilter(field_name='producto', lookup_expr='icontains', label='Producto', widget=forms.TextInput(attrs={'placeholder': 'Buscar'}))
    precio__gte = NumberFilter(field_name='precio', lookup_expr='gte', label='Precio mínimo', widget=forms.TextInput(attrs={'placeholder': '$', 'type':'number'}))
    precio__lte = NumberFilter(field_name='precio', lookup_expr='lte', label='Precio máximo', widget=forms.TextInput(attrs={'placeholder': '$', 'type':'number'}))
    id_marca = ModelChoiceFilter(field_name='id_marca', label='Marca', queryset=Marca.objects.all(), empty_label='Seleccionar' )

    class Meta:
        model = Producto
        fields = ['producto', 'id_marca']