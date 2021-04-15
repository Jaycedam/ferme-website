from django.contrib import admin
from .models import Persona, Domicilio, FamiliaProducto, TipoProducto, Producto, Proveedor, Rubro
from django.contrib.auth.models import User

# Register your models here.

class PersonaAdmin(admin.ModelAdmin):
    list_display = ["rut_persona", "usuario"]


class RubroAdmin(admin.ModelAdmin):
    list_display = ["rubro"]

class TipoProductoAdmin(admin.ModelAdmin):
    list_display = ["tipo_producto"]

admin.site.register(Persona, PersonaAdmin)
admin.site.register(Domicilio)
admin.site.register(FamiliaProducto)
admin.site.register(TipoProducto, TipoProductoAdmin)
admin.site.register(Producto)
admin.site.register(Proveedor)
admin.site.register(Rubro, RubroAdmin)

admin.site.site_header = 'Administración Ferme'
admin.site.site_title = 'Ferme'
admin.site.index_title = 'Sitio administrativo Ferme'