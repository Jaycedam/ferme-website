from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from .models import *

# Register your models here.

# CONFIG GENERAL DE ADMIN
admin.site.site_header = 'Administración Ferme'
admin.site.site_title = 'Ferme'
admin.site.index_title = 'Sitio administrativo Ferme'

# ADMIN DE LISTADOS SIN PERSONALIZACION
admin.site.register(FamiliaProducto)
admin.site.register(Persona)
admin.site.register(Proveedor)
admin.site.register(Domicilio)
admin.site.register(Marca)
admin.site.register(Producto)
admin.site.register(Rubro)
admin.site.register(TipoProducto)

