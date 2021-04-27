import django_filters
from django_filters import CharFilter, NumberFilter, ModelChoiceFilter
from .get_family_id import get_current_id
from .models import Producto, TipoProducto


class ProductoFilter(django_filters.FilterSet): 
    producto = CharFilter(field_name='producto', lookup_expr='icontains', label='Nombre producto')
    precio__gte = NumberFilter(field_name='precio', lookup_expr='gte', label='Precio mínimo')
    precio__lte = NumberFilter(field_name='precio', lookup_expr='lte', label='Precio máximo')
    id_tipo_producto = ModelChoiceFilter(field_name='id_tipo_producto', label='Tipo producto', queryset=TipoProducto.objects.all())

    class Meta:
        model = Producto
        fields = ['producto']

