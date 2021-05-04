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
    def clean_rut(self):
        users = Persona.objects.all()
        rut = self.cleaned_data["rut"]

        for u in users:
            if u.rut_persona == rut:
                raise ValidationError("Este rut ya está registrado")
        return rut

    rut_persona = forms.CharField(min_length=10, max_length=10, required=True, label="Rut (sin puntos con guión)")

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
    rut_persona = forms.CharField(disabled=True, label="Rut")
    celular = forms.IntegerField()
    class Meta:
        model = Persona
        fields = ["rut_persona", "celular",]

class ProfileAdressForm(forms.ModelForm):
    class Meta:
        model = Domicilio
        fields = ["calle", "nro",]

class ProductRequestForm(forms.ModelForm):
    id_proveedor = forms.ModelChoiceField(queryset=Proveedor.objects.all(), label="Proveedor")
    id_producto = forms.ModelChoiceField(queryset=Producto.objects.all(), label="Producto")
    class Meta: 
        model = OcDetalle
        fields = ["id_proveedor", "id_producto"]

