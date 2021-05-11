from .forms import CustomUserCreationForm, ProfileForm, ModifyUserForm, ModifyProfileForm, ProductForm, AdressForm, ProductModifyForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render, redirect, get_object_or_404
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import Persona, User, FamiliaProducto, Producto, TipoProducto, Domicilio
from .filters import ProductoFilter, ProductAdminFilter, UsuarioAdminFilter
from django.contrib import messages

# Create your views here.

# SECCIÓN ADMIN
def admin(request):
    return render(request, '/admin/')

def admin_home(request):
    return render(request, 'app/admin/home.html')

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

# SECCION USUARIO GENERAL
def home(request):
    familia_producto = FamiliaProducto.objects.all()

    data = {
        "familia_producto":familia_producto
    }

    return render(request, 'app/shop/home.html', data)

def profile(request):
    user = request.user

    data = {
        "user":user,
    }

    if Persona.objects.filter(usuario=user).exists():
        profile = Persona.objects.get(usuario=user)
        data["profile"] = profile

        if Domicilio.objects.filter(rut_persona=profile.rut_persona).exists():
            data["domicilio"] = Domicilio.objects.get(rut_persona=profile.rut_persona) 
        else:
            data["form"] = AdressForm(instance=profile)

    if request.method == 'POST':
        form = AdressForm(data=request.POST)

        if form.is_valid():
            adress_form = form.save(commit=False)
            adress_form.rut_persona = profile

            adress_form.save()
            messages.success(request, "Domicilio registrado correctamente")
            return redirect(to="profile")

        data["form"] = form

    return render(request, 'app/profile/profile.html', data)

def adress_modify(request):
    profile = Persona.objects.get(usuario=request.user)

    adress = Domicilio.objects.get(rut_persona=profile)

    data = {
        'form':AdressForm(instance=adress)
    }

    if request.method == 'POST':
        form = AdressForm(data=request.POST, instance=adress)

        if form.is_valid():
            new_adress = form.save(commit=False)

            new_adress.rut_persona = profile
            new_adress.save()
            messages.success(request, "Domicilio modificado correctamente")
            return redirect(to="profile")

        data["form"] = form

    return render(request, 'app/profile/adress_modify.html', data)

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
            messages.success(request, "Perfil modificado correctamente")
            return redirect(to="profile")

        data["form"] = form
        data["profile_form"] = profile_form
    return render(request, 'app/profile/profile_modify.html', data)

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
            return redirect(to="home")
        data["form"] = form
        data["profile_form"] = profile_form

    return render(request, 'registration/register.html', data)

def products(request, id):
    products = Producto.objects.filter(id_tipo_producto__id_familia_producto=id, stock__gt=0)

    family = FamiliaProducto.objects.get(id_familia_producto=id)

    productsFiltered = ProductoFilter(request.GET, queryset=products)

    products = productsFiltered.qs

    data = {
        "products":products,
        "family":family,
        "productsFiltered":productsFiltered,
    }

    return render(request, 'app/shop/products.html', data)

def product(request, id):
    producto = Producto.objects.get(id_producto=id)

    data = {
        "producto":producto
    }

    return render(request, 'app/shop/product.html', data)

def cart(request):

    return render(request, 'app/shop/cart.html')

# SECCION EMPLEADO
def product_management(request):
    productos = Producto.objects.all()
    productosFiltered = ProductAdminFilter(request.GET, queryset=productos)
    productos = productosFiltered.qs

    form = ProductForm()

    data = {
        "form":form,
        "productos":productos,
        "productosFiltered":productosFiltered
    }

    if request.method == 'POST':
        form = ProductForm(data=request.POST, files=request.FILES)

        if form.is_valid():
            form.save()
            messages.success(request, "Producto registrado correctamente")

        data["form"] = form

    return render(request, 'app/employee/product_management.html', data)

def product_modify(request, id):
    product = get_object_or_404(Producto, id_producto=id)

    data = {
        'form':ProductModifyForm(instance=product)
    }

    if request.method == 'POST':
        form = ProductModifyForm(data=request.POST, instance=product)

        if form.is_valid():
            form.save()

            messages.success(request, "Producto modificado correctamente")
            return redirect(to="product_management")

        data["form"] = form

    return render(request, 'app/employee/product_modify.html', data)