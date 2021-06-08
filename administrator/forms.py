from django import forms
from datetime import datetime
from django.forms import ValidationError
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Proveedor, Rubro, Marca, FamiliaProducto, TipoProducto

class ProviderForm(forms.ModelForm):
    nombre_empresa = forms.CharField(label="Nombre empresa", min_length=3, max_length=50, required=False)
    id_rubro = forms.ModelChoiceField(queryset=Rubro.objects.all(), label='Rubro', empty_label='Seleccionar', required=False)
    class Meta:
        model = Proveedor
        fields = ["nombre_empresa", "id_rubro"]

    def __init__(self, *args, **kwargs):
        super(ProviderForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

class AdminUserForm(UserCreationForm):
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

    username = forms.CharField(label="Nombre de usuario")
    first_name = forms.CharField(min_length=3, max_length=80, required=True, label="Nombre")
    last_name = forms.CharField(min_length=3, max_length=80, required=True, label="Apellido")
    email = forms.EmailField(required=True, label="Correo electrónico")
    is_staff = forms.ChoiceField(label='Es empleado', choices = {(False,"No"),(True,"Sí")})
    is_superuser = forms.ChoiceField(label='Es superusuario', choices = {(True,"Sí"),(False,"No")})

    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email", "is_staff", "is_superuser", "password1", "password2"]

    def __init__(self, *args, **kwargs):
        super(AdminUserForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

class AdminModifyUserForm(forms.ModelForm):
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

    username = forms.CharField(label="Nombre de usuario")
    first_name = forms.CharField(min_length=3, max_length=80, required=True, label="Nombre")
    last_name = forms.CharField(min_length=3, max_length=80, required=True, label="Apellido")
    email = forms.EmailField(required=True, label="Correo electrónico")
    is_staff = forms.ChoiceField(label='Es empleado', choices = {(False,"No"),(True,"Sí")})
    is_superuser = forms.ChoiceField(label='Es superusuario', choices = {(True,"Sí"),(False,"No")})

    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email", "is_staff", "is_superuser"]

    def __init__(self, *args, **kwargs):
        super(AdminModifyUserForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

class BrandForm(forms.ModelForm):
    class Meta:
        model = Marca
        fields = ["marca"]

class CategoryAdminForm(forms.ModelForm):
    class Meta:
        model = FamiliaProducto
        fields = ["familia_producto", "imagen_url"]

class SubCategoryForm(forms.ModelForm):
    class Meta:
        model = TipoProducto
        fields = ["tipo_producto", "id_familia_producto"]