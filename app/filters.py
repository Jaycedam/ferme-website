import django_filters
from django_filters import CharFilter, NumberFilter, ModelChoiceFilter

from .models import Producto, TipoProducto, FamiliaProducto

class ProductoFilter(django_filters.FilterSet):
    # agregar código para recoger id de familia seleccionada
    #id_familia = 
    #id_tipo_producto_filtered = ModelChoiceFilter(field_name='id_tipo_producto', label='Tipo producto', queryset=TipoProducto.objects.filter(id_familia_producto=id_familia))

    producto = CharFilter(field_name='producto', lookup_expr='icontains', label='Nombre producto')
    precio__gte = NumberFilter(field_name='precio', lookup_expr='gte', label='Precio mínimo')
    precio__lte = NumberFilter(field_name='precio', lookup_expr='lte', label='Precio máximo')
    id_tipo_producto = ModelChoiceFilter(field_name='id_tipo_producto', label='todos los tipos de producto', queryset=TipoProducto.objects.all())


    class Meta:
        model = Producto
        fields = ['producto', 'id_tipo_producto']