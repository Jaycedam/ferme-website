from django import forms
from datetime import datetime
from django.forms import ValidationError
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Producto

class ProductForm(forms.ModelForm):
    def clean_stock(self):
        stock = self.cleaned_data["stock"]
        if stock < 0:
            raise ValidationError("Ingresa un stock válido")
        return stock

    def clean_stock_critico(self):
        stock_critico = self.cleaned_data["stock_critico"]
        if stock_critico < 0:
            raise ValidationError("Ingresa un stock válido")
        return stock_critico

    producto = forms.CharField(label="Nombre", min_length=3, max_length=50)
    fecha_vencimiento = forms.DateField(label="Fecha vencimiento (dd/mm/yy)", required=False)
    imagen_url = forms.FileField(label="Imagen", required=False)
    class Meta: 
        model = Producto
        fields = ["producto", "descripcion", "precio", "precio_proveedor", "stock", "stock_critico", "fecha_vencimiento", "id_tipo_producto", "id_proveedor", "id_marca", "imagen_url"]

class ProductModifyForm(forms.ModelForm):
    class Meta: 
        model = Producto
        fields = ["producto", "descripcion", "precio", "precio_proveedor", "stock", "stock_critico", "imagen_url"]

