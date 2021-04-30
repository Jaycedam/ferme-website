from .forms import CustomUserCreationForm, ProfileForm, ModifyUserForm, ModifyProfileForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render, redirect, get_object_or_404
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import Persona, User, FamiliaProducto, Producto, TipoProducto
from .filters import ProductoFilter, ProductoAdminFilter, UsuarioAdminFilter
from django.contrib import messages

# Create your views here.

def admin(request):
    return render(request, '/admin/')

def admin_home(request):
    return render(request, 'app/admin/home.html')

def admin_productos(request):
    productos = Producto.objects.all()
    productosFiltered = ProductoAdminFilter(request.GET, queryset=productos)
    productos = productosFiltered.qs

    data = {
        "productos":productos,
        "productosFiltered":productosFiltered
    }

    return render(request, 'app/admin/productos.html', data)

def admin_usuarios(request):
    usuarios = Persona.objects.all().select_related('usuario')
    usuariosFiltered = UsuarioAdminFilter(request.GET, queryset=usuarios)
    usuarios = usuariosFiltered.qs

    data = {
        "usuarios":usuarios,
        "usuariosFiltered":usuariosFiltered,
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

            messages.success(request, "Usuario creado correctamente")

        data["form"] = form
        data["profile_form"] = profile_form

    return render(request, 'app/admin/usuarios.html', data)

def home(request):
    familia_producto = FamiliaProducto.objects.all()

    data = {
        "familia_producto":familia_producto
    }

    return render(request, 'app/home.html', data)

def profile(request):
    user = request.user

    try:
        persona = Persona.objects.get(usuario=user.id)

        data = {
            "persona":persona,
            "user":user
        }

    except:
        data = {
            "user":user
        }

    return render(request, 'app/profile/profile.html', data)

def profile_modify(request):
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
    return render(request, 'app/profile/modify.html', data)

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

def products(request, id):
    productos = Producto.objects.filter(id_tipo_producto__id_familia_producto=id)

    familia = FamiliaProducto.objects.get(id_familia_producto=id)


    #pasar parametro "id_familia" a myFilter()
    productosFiltered = ProductoFilter(request.GET, queryset=productos)

    productos = productosFiltered.qs

    data = {
        "productos":productos,
        "familia":familia,
        "productosFiltered":productosFiltered,
    }

    return render(request, 'app/products/products.html', data)

def product(request, id):
    producto = Producto.objects.get(id_producto=id)

    data = {
        "producto":producto
    }

    return render(request, 'app/products/product.html', data)

def cart(request):

    return render(request, 'app/cart.html')