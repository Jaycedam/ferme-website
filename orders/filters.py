import django_filters
from django_filters import CharFilter, NumberFilter, ModelChoiceFilter
from .models import Orden, Proveedor, Estado
from django import forms

class OrdersFilter(django_filters.FilterSet): 
    nro_orden = CharFilter(field_name='nro_orden', lookup_expr='icontains', label='Buscar', widget=forms.TextInput(attrs={'placeholder': 'N° orden'}) )
    id_estado = ModelChoiceFilter(field_name='id_estado', label='Estado', queryset=Estado.objects.all(), empty_label='' )

    class Meta:
        model = Orden
        fields = ['nro_orden', 'id_estado']

class OrderToProviderFilter(django_filters.FilterSet): 
    nro_orden = CharFilter(field_name='nro_orden', lookup_expr='icontains', label='Buscar', widget=forms.TextInput(attrs={'placeholder': 'N° orden'}) )
    id_proveedor = ModelChoiceFilter(field_name='id_proveedor', label='Proveedor', queryset=Proveedor.objects.all(), empty_label='' )
    id_estado = ModelChoiceFilter(field_name='id_estado', label='Estado', queryset=Estado.objects.all(), empty_label='' )

    class Meta:
        model = Orden
        fields = ['nro_orden', 'id_proveedor', 'id_estado']