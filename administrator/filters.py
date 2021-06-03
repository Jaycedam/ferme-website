import django_filters
from django_filters import CharFilter, NumberFilter, ModelChoiceFilter, ChoiceFilter
from .models import Persona, User
from django import forms

class UsuarioAdminFilter(django_filters.FilterSet):
    persona__rut_persona = CharFilter(label='Rut persona', lookup_expr='icontains', widget=forms.TextInput(attrs={'placeholder': 'Sin puntos con guión'}) )
    email = CharFilter(label='Email', lookup_expr='icontains', widget=forms.TextInput(attrs={'placeholder': '@'}) )
    username = CharFilter(label='Nombre de usuario', lookup_expr='icontains', widget=forms.TextInput(attrs={'placeholder': 'username'}) )

    is_staff = ChoiceFilter(label='Es empleado', choices = {(True,"Sí"),(False,"No")}, empty_label='Seleccionar' )
    is_superuser = ChoiceFilter(label='Es superusuario', choices = {(True,"Sí"),(False,"No")}, empty_label='Seleccionar' )

    class Meta:
        model = User
        fields = ['username', 'email', 'is_staff', 'is_superuser', 'persona__rut_persona']
