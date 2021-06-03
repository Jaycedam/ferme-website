from django import forms
from datetime import datetime
from django.forms import ValidationError
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Proveedor, Rubro

class ProviderForm(forms.ModelForm):
    nombre_empresa = forms.CharField(label="Nombre empresa", min_length=3, max_length=50, required=False)
    id_rubro = forms.ModelChoiceField(queryset=Rubro.objects.all(), label='Rubro', empty_label='', required=False)
    class Meta:
        model = Proveedor
        fields = ["nombre_empresa", "id_rubro"]

    def __init__(self, *args, **kwargs):
        super(ProviderForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'



