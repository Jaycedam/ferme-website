from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from .models import *
import nested_admin

# Register your models here.

# CONFIG GENERAL DE ADMIN
admin.site.site_header = 'Administración Ferme'
admin.site.site_title = 'Ferme'
admin.site.index_title = 'Sitio administrativo Ferme'

# ADMIN DE USER-PERSONA-DOMICILIO // PROVEEDOR INLINE
class DomicilioInline(nested_admin.NestedTabularInline):
    model = Domicilio

class ProveedorInline(nested_admin.NestedTabularInline):
    model = Proveedor

class PersonaAdmin(nested_admin.NestedModelAdmin):
    model = Persona
    inlines = [DomicilioInline,ProveedorInline,]

admin.site.register(Persona, PersonaAdmin)

# ADMIN DE ORDEN-DETALLE-RECIBO INLINE
class OrdenDetalleInline(nested_admin.NestedTabularInline):
    model = OrdenDetalle

class ReciboInline(nested_admin.NestedTabularInline):
    model = Recibo

class OrdenAdmin(nested_admin.NestedModelAdmin):
    list_display = ['nro_orden', 'fecha', 'total', 'rut_persona',]
    list_filter = ['id_tipo',]
    search_fields = ['nro_orden',]
    inlines = [OrdenDetalleInline,ReciboInline]

admin.site.register(Orden, OrdenAdmin)

# ADMIN DE LISTADOS SIN PERSONALIZACION
admin.site.register(FamiliaProducto)
admin.site.register(Marca)
admin.site.register(Producto)
admin.site.register(Rubro)
admin.site.register(TipoProducto)

