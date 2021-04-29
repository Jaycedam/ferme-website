from .forms import CustomUserCreationForm, ProfileForm, ModifyUserForm, ModifyProfileForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render, redirect, get_object_or_404
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import Persona, User, FamiliaProducto, Producto, TipoProducto
from .filters import ProductoFilter

# Create your views here.

def admin(request):
    return render(request, '/admin/')

def administrador(request):
    return render(request, 'app/administrador.html')

def inicio(request):
    familia_producto = FamiliaProducto.objects.all()

    data = {
        "familia_producto":familia_producto
    }

    return render(request, 'app/inicio.html', data)

def perfil(request):
    current_user = request.user

    try:
        persona = Persona.objects.get(usuario=current_user.id)

        data = {
            "persona":persona,
            "user":current_user
        }

    except:
        data = {
            "user":current_user
        }

    return render(request, 'app/perfil/perfil.html', data)

def modificar_perfil(request):
    user = request.user

    if Persona.objects.filter(usuario=request.user).exists():
        profile = Persona.objects.get(usuario=user)

        data = {
            'form': ModifyUserForm(instance=user),
            'profile_form': ModifyProfileForm(instance=profile)
        }      

    else:
        data = {
            'form': ModifyUserForm(instance=user),
        }   


    if request.method == 'POST':
        form = ModifyUserForm(data=request.POST, instance=user)
        profile_form = ModifyProfileForm(data=request.POST, instance=profile)

        if form.is_valid() and profile_form.is_valid():
            usuario = form.save()
            prof = profile_form.save(False)

            prof.usuario = request.user
            prof.save()

            return redirect(to="perfil")

        data["form"] = form
        data["profile_form"] = profile_form

    return render(request, 'app/perfil/modificar.html', data)

def register(request):
    data = {
        'form': CustomUserCreationForm(),
        'profile_form': ProfileForm()
    }

    if request.method == 'POST':
        form = CustomUserCreationForm(data=request.POST)
        profile_form = ProfileForm(data=request.POST)

        if form.is_valid() and profile_form.is_valid():
            usuario = form.save()
            profile = profile_form.save(commit=False)

            profile.usuario = usuario

            profile.save()

            user = authenticate(username=form.cleaned_data["username"],
                password=form.cleaned_data["password1"]
            )
            login(request, user)
            return redirect(to="inicio")
        data["form"] = form
        data["profile_form"] = profile_form

    return render(request, 'registration/register.html', data)

def productos(request, id):
    productos = Producto.objects.filter(id_tipo_producto__id_familia_producto=id)

    familia = FamiliaProducto.objects.get(id_familia_producto=id)

    #pasar parametro "id_familia" a myFilter()
    myFilter = ProductoFilter(request.GET, queryset=productos)
    
    productos = myFilter.qs

    data = {
        "productos":productos,
        "familia":familia,
        "myFilter":myFilter,
    }

    return render(request, 'app/productos/productos.html', data)

def producto(request, id):
    producto = Producto.objects.get(id_producto=id)

    data = {
        "producto":producto
    }

    return render(request, 'app/productos/producto.html', data)

def cart(request):

    return render(request, 'app/cart.html')