import django_filters
from django_filters import CharFilter, NumberFilter, ModelChoiceFilter
from .models import Orden, Proveedor, Estado
from django import forms

class OrdersFilter(django_filters.FilterSet): 
    nro_orden = CharFilter(field_name='nro_orden', lookup_expr='icontains', label='N° Orden', widget=forms.TextInput(attrs={'placeholder': 'Buscar'}) )
    id_estado = ModelChoiceFilter(field_name='id_estado', label='Estado', queryset=Estado.objects.all(), empty_label='Seleccionar' )

    class Meta:
        model = Orden
        fields = ['nro_orden', 'id_estado']

class OrderToProviderFilter(django_filters.FilterSet): 
    nro_orden = CharFilter(field_name='nro_orden', lookup_expr='icontains', label='N° Orden', widget=forms.TextInput(attrs={'placeholder': 'Buscar'}) )
    id_proveedor = ModelChoiceFilter(field_name='id_proveedor', label='Proveedor', queryset=Proveedor.objects.all(), empty_label='Seleccionar' )
    id_estado = ModelChoiceFilter(field_name='id_estado', label='Estado', queryset=Estado.objects.all(), empty_label='Seleccionar' )

    class Meta:
        model = Orden
        fields = ['nro_orden', 'id_proveedor', 'id_estado']