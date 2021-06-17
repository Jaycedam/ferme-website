from .forms import *
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.http import Http404
from .filters import ProductoFilter
from django.contrib import messages
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from .utils import cookieCart
import datetime
from django.core.paginator import Paginator
from email_sender.views import send_order_email

# Create your views here.

# SECCIÓN ADMIN
def admin(request):
    return render(request, '/admin/')

# SECCION USUARIO GENERAL
def home(request):
    familia_producto = FamiliaProducto.objects.all()

    data = {
        "familia_producto":familia_producto
    }

    # mandamos data si el usuario es proveedor
    try:
        data['provider'] = Proveedor.objects.get(rut_persona=Persona.objects.get(usuario=request.user))
    except:
        pass

    return render(request, 'shop/shop/home.html', data)

@login_required
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
        
        if Proveedor.objects.filter(rut_persona=profile).exists():
            data['provider'] = Proveedor.objects.get(rut_persona=profile)

    if request.method == 'POST':
        form = AdressForm(data=request.POST)

        if form.is_valid():
            adress_form = form.save(commit=False)
            adress_form.rut_persona = profile

            adress_form.save()
            messages.success(request, "Domicilio registrado correctamente")
            return redirect(to="profile")

        data["form"] = form

    return render(request, 'shop/profile/profile.html', data)

@login_required
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
            messages.success(request, "Tu perfil ha sido actualizado")
            return redirect(to="profile")

        data["form"] = form

    return render(request, 'shop/profile/adress_modify.html', data)

@login_required
def profile_modify(request):
    user = request.user

    # si existe el perfil de usuario, se instancia el form con los datos actuales
    if Persona.objects.filter(usuario=request.user).exists():
        profile = Persona.objects.get(usuario=user)
        instanced = True

        data = {
            'form': ModifyUserForm(instance=user),
            'profile_form': ModifyProfileForm(instance=profile)
        }      

    # si no existe, se crea un nuevo form de perfil
    if not Persona.objects.filter(usuario=request.user).exists():
        instanced = False
        data = {
            'form': ModifyUserForm(instance=user),
            'profile_form': ProfileForm()
        }   

    if request.method == 'POST':
        form = ModifyUserForm(data=request.POST, instance=user)
        # si es instanciado, se actualiza, si no existe se crea
        if instanced:
            profile_form = ModifyProfileForm(data=request.POST, instance=profile)
        if not instanced:
            profile_form = ProfileForm(data=request.POST)

        if form.is_valid() and profile_form.is_valid():
            usuario = form.save()
            prof = profile_form.save(False)

            prof.usuario = usuario
            prof.save()
            messages.success(request, "Tu perfil ha sido actualizado")
            return redirect(to="profile")

        data["form"] = form
        data["profile_form"] = profile_form
    return render(request, 'shop/profile/profile_modify.html', data)

@login_required
def provider_modify(request):
    profile = Persona.objects.get(usuario=request.user)

    provider = Proveedor.objects.get(rut_persona=profile)

    data = {
        'form':ModifyProviderForm(instance=provider)
    }

    if request.method == 'POST':
        form = ModifyProviderForm(data=request.POST, instance=provider)

        if form.is_valid():
            new_provider = form.save(commit=False)

            new_provider.rut_persona = profile
            new_provider.save()
            messages.success(request, "Tu perfil ha sido actualizado")
            return redirect(to="profile")

        data["form"] = form

    return render(request, 'shop/profile/provider_modify.html', data)

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
    family = FamiliaProducto.objects.get(id_familia_producto=id)
    productsFiltered = ProductoFilter(request.GET, queryset=Producto.objects.filter(id_tipo_producto__id_familia_producto=id, stock__gt=0))
    products = productsFiltered.qs

    paginator = Paginator(products, 20)
    page_number = request.GET.get('page', 1)
    page = paginator.get_page(page_number)


    data = {
        "entity":page,
        "family":family,
        "productsFiltered":productsFiltered,
    }

    return render(request, 'shop/shop/products.html', data)

def product(request, id):
    producto = Producto.objects.get(id_producto=id)

    data = {
        "producto":producto
    }

    return render(request, 'shop/shop/product.html', data)

def cart(request):
    cart = cookieCart(request)
    
    order = cart['order']
    items = cart['items']

    data = {
        'items':items, 
        'order':order
        }
    try:
        data['profile'] = Persona.objects.get(usuario=request.user)
    except:
        pass

    return render(request, 'shop/shop/cart.html', data)

# Aprobar datos de compra y delivery
@login_required
def checkout(request):
   
    tipoDoc = TipoDocumento.objects.all()

    cart = cookieCart(request)
    
    order = cart['order']
    items = cart['items']

    data = {
        'items':items, 
        'order':order,
        'tipoDoc':tipoDoc,
        }
        
    if Persona.objects.filter(usuario=request.user).exists():
        profile = Persona.objects.get(usuario=request.user)
        data['profile'] = profile

        if Domicilio.objects.filter(rut_persona=profile.rut_persona).exists():
            data['adress'] = Domicilio.objects.get(rut_persona=profile.rut_persona)


    # Recibimos tipo documento y guardamos en bd la compra
    if request.method == 'POST':
        id_tipo_doc = request.POST.get('tipoDoc')
        subtotal = order['get_cart_total']
                
        try:
            domicilio = Domicilio.objects.get(rut_persona=profile)

            new_order = Orden.objects.create(
                fecha=datetime.datetime.now(), 
                total=subtotal, 
                # guardamos orden como tipo Cliente
                id_tipo=TipoOrden.objects.get(id_tipo=1), 
                rut_persona=Persona.objects.get(rut_persona=profile),
                # asignamos orden como pendiente
                id_estado=Estado.objects.get(id_estado=1)
                )

            Delivery.objects.create(
                nro_orden = new_order,
                calle = domicilio.calle,
                nro = domicilio.nro,
                nro_departamento = domicilio.nro_departamento,
                id_comuna = domicilio.id_comuna
            )

            # loop de items en cookieCart
            for i in items:
                # instanciamos un producto desde el valor del carro de compra 
                producto = Producto.objects.get(id_producto=i['product']['id'])

                if i['quantity'] > producto.stock:
                    raise Exception

                OrdenDetalle.objects.create(
                    id_producto = producto,
                    precio=producto.precio,
                    cantidad = i['quantity'],
                    total = i['get_total'],
                    nro_orden = new_order
                )

            # Datos para boleta/factura
            iva = 0
            # definir iva si es factura
            if id_tipo_doc == "2":
                iva = round(subtotal*0.19)
            total = subtotal+iva

            recibo = Recibo.objects.create(
                fecha = datetime.datetime.now(),
                subtotal = subtotal,
                iva = iva,
                total = total,
                id_tipo = TipoDocumento.objects.get(id_tipo=id_tipo_doc),
                nro_orden = new_order,
            )

            # si todo funciona cambiamos el estado de la orden a confirmada
            new_order.id_estado=Estado.objects.get(id_estado=2)
            new_order.save()

            send_order_email(request.user.email, new_order)
            messages.success(request, "Tu compra ha sido confirmada")

        except Exception as e:
            print(e)
            if new_order:
                new_order.id_estado = Estado.objects.get(id_estado=3)
                new_order.save()

            messages.error(request, "No se ha podido realizar la compra, intenta nuevamente")

        return redirect(to="home")
    return render(request, 'shop/shop/checkout.html', data)
