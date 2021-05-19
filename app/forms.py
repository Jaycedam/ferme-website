from django import forms
from datetime import datetime
from django.forms import ValidationError
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Persona, OrdenCompra, Proveedor, OcDetalle, Domicilio, Producto, TipoProducto


class CustomUserCreationForm(UserCreationForm):
    def clean_first_name(self):
        first_name = self.cleaned_data["first_name"]
        if str(first_name).isalpha():
            return first_name
        raise ValidationError("Ingrese sólo letras")

    def clean_last_name(self):
        last_name = self.cleaned_data["last_name"]
        if str(last_name).isalpha():
            return last_name
        raise ValidationError("Ingrese sólo letras")

    def clean_email(self):
        users = User.objects.all()
        email = self.cleaned_data["email"]

        for u in users:
            if u.email == email:
                raise ValidationError("Este mail ya está registrado")
        return email

    first_name = forms.CharField(min_length=3, max_length=80, required=True, label="Nombre")
    last_name = forms.CharField(min_length=3, max_length=80, required=True, label="Apellido")
    email = forms.EmailField(required=True, label="Correo electrónico")

    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email", "password1", "password2"]

class ProfileForm(forms.ModelForm):
    def clean_rut_persona(self):
        users = Persona.objects.all()
        rut = self.cleaned_data["rut_persona"]

        if len(rut) != 10:
            raise ValidationError("Formato incorrecto")
        if len(rut) == 10 and rut[-2] != "-":
            raise ValidationError("Formato incorrecto")

        for u in users:
            if u.rut_persona == rut:
                raise ValidationError("Este rut ya está registrado")
        return rut
    
    def clean_celular(self):
        celular = self.cleaned_data["celular"]
        if len(str(celular)) != 9:
            raise ValidationError("No están todos los dígitos")
        if str(celular)[0] != "9":
            raise ValidationError("Formato incorrecto, el celular debe comenzar con 9")
        return celular

    rut_persona = forms.CharField(min_length=10, max_length=10, required=True, label="Rut (sin puntos con guión)")
    celular = forms.IntegerField(required=True, label="Celular (912345678)")

    class Meta:
        model = Persona
        fields = ["rut_persona", "celular"]

class AdressForm(forms.ModelForm):
    class Meta: 
        model = Domicilio
        fields = ["id_comuna", "id_tipo_domicilio", "calle", "nro", "nro_departamento"]

class ModifyUserForm(forms.ModelForm):
    def clean_first_name(self):
        first_name = self.cleaned_data["first_name"]
        if str(first_name).isalpha():
            return first_name
        raise ValidationError("Ingrese sólo letras")

    def clean_last_name(self):
        last_name = self.cleaned_data["last_name"]
        if str(last_name).isalpha():
            return last_name
        raise ValidationError("Ingrese sólo letras")

    username = forms.CharField(disabled=True, label="Nombre de usuario")
    first_name = forms.CharField(min_length=3, max_length=80, required=True, label="Nombre")
    last_name = forms.CharField(min_length=3, max_length=80, required=True, label="Apellido")
    email = forms.EmailField(required=True, label="Correo electrónico")

    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email"]

class ModifyProfileForm(forms.ModelForm):
    def clean_celular(self):
        celular = self.cleaned_data["celular"]
        if len(str(celular)) != 9:
            raise ValidationError("No están todos los dígitos")
        if str(celular)[0] != "9":
            raise ValidationError("Formato incorrecto, el celular debe comenzar con 9")
        return celular

    rut_persona = forms.CharField(disabled=True, label="Rut")
    celular = forms.IntegerField(required=True, label="Celular (912345678)")
    
    class Meta:
        model = Persona
        fields = ["rut_persona", "celular",]

class ProfileAdressForm(forms.ModelForm):
    class Meta:
        model = Domicilio
        fields = ["calle", "nro",]

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
    fecha_vencimiento = forms.DateField(label="Fecha vencimiento (dd/mm/yy)")
    imagen_url = forms.FileField(label="Imagen", required=False)
    class Meta: 
        model = Producto
        fields = ["producto", "descripcion", "precio", "precio_proveedor", "stock", "stock_critico", "fecha_vencimiento", "id_tipo_producto", "id_proveedor", "id_marca", "imagen_url"]

class ProductModifyForm(forms.ModelForm):
    class Meta: 
        model = Producto
        fields = ["producto", "descripcion", "precio", "precio_proveedor", "stock", "stock_critico", "imagen_url"]
