from django.shortcuts import render, redirect
from .models import *
from shop.forms import CustomUserCreationForm, ProfileForm, AdressForm
from .forms import *
from django.contrib import messages
from .filters import UsuarioAdminFilter

# Create your views here.
def home(request):
    return render(request, 'administrator/home.html')


def users(request):
    users = User.objects.select_related('persona').all()
    users_filtered = UsuarioAdminFilter(request.GET, queryset=users)
    users = users_filtered.qs

    data = {
        'users':users,
        'users_filtered':users_filtered
    }
    return render(request, 'administrator/user/list.html', data)

def create_user(request):
    data = {
        'form': CustomUserCreationForm(),
        'profile_form': ProfileForm(),
        'provider_form': ProviderForm(),
    }

    if request.method == 'POST':
        form = CustomUserCreationForm(data=request.POST)
        profile_form = ProfileForm(data=request.POST)
        provider_form = ProviderForm(data=request.POST)
        
        # creamos variable is_staff en False por defecto, 
        is_staff = False
        # si el checkbox de empleado está en "on" se guarda True
        if request.POST.get('is_staff') == "on":
            is_staff = True

        # verificamos si el checkbox de proveedor está checkeado
        is_provider = False
        if request.POST.get('is_provider') == "on":
            is_provider = True
        
        if is_provider:
            # si es proveedor y los datos son nulos, retornar mensaje error
            if request.POST.get('nombre_empresa')=='' or request.POST.get('id_rubro')=='':
                messages.error(request, "No se puede crear un proveedor con datos nulos")
                return redirect(to="admin_create_user")
            print("still happens")

            if form.is_valid() and profile_form.is_valid() and provider_form.is_valid():
                usuario = form.save(commit=False)
                usuario.is_staff = is_staff
                usuario.save()

                profile = profile_form.save(commit=False)
                profile.usuario = usuario
                profile.save()

                provider = provider_form.save(commit=False)
                provider.rut_persona = profile
                provider.save()

                messages.success(request, f"Usuario {usuario.username} creado correctamente")
                return redirect(to="admin_users")

        if not is_provider:
            if form.is_valid() and profile_form.is_valid():
                usuario = form.save(commit=False)
                usuario.is_staff = is_staff
                usuario.save()

                profile = profile_form.save(commit=False)
                profile.usuario = usuario
                profile.save()

                messages.success(request, f"Usuario {usuario.username} creado correctamente")
                return redirect(to="admin_users")
        data["form"] = form
        data["profile_form"] = profile_form
        data["provider_form"] = provider_form

    return render(request, 'administrator/user/create.html', data)

def modify_user(request, id):
    data = {}
    return render(request, 'administrator/user/modify.html', data)