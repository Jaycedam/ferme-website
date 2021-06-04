from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from shop.forms import CustomUserCreationForm, ProfileForm, AdressForm, ModifyUserForm, ModifyProfileForm, ModifyProviderForm
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
        'title': 'Crear usuario',
        'form': AdminUserForm(),
        'profile_form': ProfileForm(),
        'provider_form': ProviderForm(),
    }

    if request.method == 'POST':
        form = AdminUserForm(data=request.POST)
        profile_form = ProfileForm(data=request.POST)
        provider_form = ProviderForm(data=request.POST)

        # verificamos si el checkbox de proveedor está checkeado
        is_provider = False
        if request.POST.get('is_provider') == "on":
            is_provider = True
        
        if is_provider:
            # si es proveedor y los datos son nulos, retornar mensaje error
            if request.POST.get('nombre_empresa')=='' or request.POST.get('id_rubro')=='':
                messages.error(request, "No se puede crear un proveedor con datos nulos")
                return redirect(to="admin_create_user")

            if form.is_valid() and profile_form.is_valid() and provider_form.is_valid():
                usuario = form.save()

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
                usuario = form.save()

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
    user = get_object_or_404(User, id=id)
    profile = get_object_or_404(Persona, usuario=user)

    data = {
        'title': 'Modificar usuario',
        'form': AdminModifyUserForm(instance=user),
        'profile_form': ModifyProfileForm(instance=profile),
    }

    try:
        provider = get_object_or_404(Proveedor, rut_persona=profile)
        data['provider_form'] = ProviderForm(instance=provider)
        instanced_provider = True
    except:
        data['provider_form'] = ProviderForm()
        instanced_provider = False


    if request.method == 'POST':
        form = AdminModifyUserForm(data=request.POST, instance=user)
        profile_form = ModifyProfileForm(data=request.POST, instance=profile)

        # verificamos si el checkbox de proveedor está checkeado
        is_provider = False
        if request.POST.get('is_provider') == "on":
            is_provider = True

        if instanced_provider:
            provider_form = ProviderForm(data=request.POST, instance=provider)
        if not instanced_provider:
            provider_form = ProviderForm(data=request.POST)


        if is_provider:
            # si es proveedor y los datos son nulos, retornar mensaje error
            if request.POST.get('nombre_empresa')=='' or request.POST.get('id_rubro')=='':
                messages.error(request, "No se puede crear un proveedor con datos nulos")
                return render(request, 'administrator/user/create.html', data)

            if form.is_valid() and profile_form.is_valid() and provider_form.is_valid():
                usuario = form.save()

                profile = profile_form.save(commit=False)
                profile.usuario = usuario
                profile.save()

                provider = provider_form.save(commit=False)
                provider.rut_persona = profile
                provider.save()

                messages.success(request, f"Usuario {usuario.username} modificado correctamente")
                return redirect(to="admin_users")

        if not is_provider:
            if form.is_valid() and profile_form.is_valid():
                usuario = form.save()

                profile = profile_form.save(commit=False)
                profile.usuario = usuario
                profile.save()

                messages.success(request, f"Usuario {usuario.username} modificado correctamente")
                return redirect(to="admin_users")
        data["form"] = form
        data["profile_form"] = profile_form
        data["provider_form"] = provider_form
    return render(request, 'administrator/user/create.html', data)