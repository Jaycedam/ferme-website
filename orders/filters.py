import django_filters
from django_filters import CharFilter, NumberFilter, ModelChoiceFilter
from .models import Orden, Proveedor, Estado
from django import forms

class OrdersFilter(django_filters.FilterSet): 
    nro_orden = CharFilter(field_name='nro_orden', lookup_expr='icontains', label='', widget=forms.TextInput(attrs={'placeholder': 'N° Orden'}) )
    id_estado = ModelChoiceFilter(field_name='id_estado', label='', queryset=Estado.objects.all(), empty_label='Seleccionar estado' )

    class Meta:
        model = Orden
        fields = ['nro_orden', 'id_estado']

class OrderToProviderFilter(django_filters.FilterSet): 
    nro_orden = CharFilter(field_name='nro_orden', lookup_expr='icontains', label='', widget=forms.TextInput(attrs={'placeholder': 'N° Orden'}) )
    id_proveedor = ModelChoiceFilter(field_name='id_proveedor', label='', queryset=Proveedor.objects.all(), empty_label='Seleccionar proveedor' )
    id_estado = ModelChoiceFilter(field_name='id_estado', label='', queryset=Estado.objects.all(), empty_label='Seleccionar estado' )

    class Meta:
        model = Orden
        fields = ['nro_orden', 'id_proveedor', 'id_estado']