from django import forms
from datetime import datetime
from django.forms import ValidationError
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Persona, Domicilio, Producto, Proveedor


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

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

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

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

class AdressForm(forms.ModelForm):
    class Meta: 
        model = Domicilio
        fields = ["id_comuna", "id_tipo_domicilio", "calle", "nro", "nro_departamento"]
    
    def __init__(self, *args, **kwargs):
        super(AdressForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

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

    username = forms.CharField(label="Nombre de usuario")
    first_name = forms.CharField(min_length=3, max_length=80, required=True, label="Nombre")
    last_name = forms.CharField(min_length=3, max_length=80, required=True, label="Apellido")
    email = forms.EmailField(required=True, label="Correo electrónico")

    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email"]

    def __init__(self, *args, **kwargs):
        super(ModifyUserForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

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

    def __init__(self, *args, **kwargs):
        super(ModifyProfileForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

class ModifyProviderForm(forms.ModelForm):

    class Meta:
        model = Proveedor
        fields = ["nombre_empresa","id_rubro"]

    def __init__(self, *args, **kwargs):
        super(ModifyProviderForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
