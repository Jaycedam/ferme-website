from .forms import *
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render, redirect, get_object_or_404
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import *
from .filters import ProductoFilter, ProductAdminFilter, UsuarioAdminFilter, ProductRequestFilter
from django.contrib import messages
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from .utils import cookieCart, cookieOrder
import datetime

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

    return render(request, 'app/shop/home.html', data)

def profile(request):
    user = request.user

    data = {
        "user":user,
    }

    if Persona.objects.filter(usuario=user).exists():
        profile = Persona.objects.get(usuario=user)
        data["profile"] = profile

        data["orders"] = Orden.objects.filter(rut_persona=profile)

        if Domicilio.objects.filter(rut_persona=profile.rut_persona).exists():
            data["domicilio"] = Domicilio.objects.get(rut_persona=profile.rut_persona) 
        else:
            data["form"] = AdressForm(instance=profile)
        
        if Proveedor.objects.filter(rut_persona=profile).exists():
            provider = Proveedor.objects.get(rut_persona=profile)
            data["provider"] = provider
            data["provider_order"] = Orden.objects.filter(id_proveedor=provider)


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

def order_details(request, id):
    doc = Recibo.objects.get(nro_orden=id)
    order = Orden.objects.get(nro_orden=id)
    order_items = OrdenDetalle.objects.filter(nro_orden=id)
    data = {
        'doc':doc,
        'order':order,
        'order_items':order_items
    }
    return render(request, 'app/profile/order_details.html', data)

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
    cart = cookieCart(request)
    
    order = cart['order']
    items = cart['items']

    data = {
        'items':items, 
        'order':order
        }

    return render(request, 'app/shop/cart.html', data)

# Aprobar datos de compra y delivery
def checkout(request):
    profile = Persona.objects.get(usuario=request.user)

    tipoDoc = TipoDocumento.objects.all()

    cart = cookieCart(request)
    
    order = cart['order']
    items = cart['items']

    data = {
        'items':items, 
        'order':order,
        'tipoDoc':tipoDoc,
        }
        
    if Domicilio.objects.filter(rut_persona=profile.rut_persona).exists():
        data['adress'] = Domicilio.objects.get(rut_persona=profile.rut_persona)

    # Recibimos tipo documento y guardamos en bd la compra
    if request.method == 'POST':
        id_tipo_doc = request.POST.get('tipoDoc')
        subtotal = order['get_cart_total']
                
        try:
            new_order = Orden.objects.create(
                fecha=datetime.datetime.now(), 
                total=subtotal, 
                # guardamos orden como tipo Cliente
                id_tipo=TipoOrden.objects.get(id_tipo=1), 
                rut_persona=Persona.objects.get(rut_persona=profile)
                )

            # loop de items en cookieCart
            for i in items:
                # instanciamos un producto desde el valor del carro de compra 
                producto = Producto.objects.get(id_producto=i['product']['id'])

                OrdenDetalle.objects.create(
                    id_producto = producto,
                    nro_orden = new_order,
                    cantidad = i['quantity'],
                    total = i['get_total']
                )

            # Datos para boleta/factura
            iva = 0
            # definir iva si es factura
            if id_tipo_doc == "2":
                iva = subtotal*0.19
            total = subtotal+iva

            recibo = Recibo.objects.create(
                fecha = datetime.datetime.now(),
                subtotal = total,
                iva = iva,
                total = total,
                id_tipo = TipoDocumento.objects.get(id_tipo=id_tipo_doc),
                nro_orden = new_order,
            )

            messages.success(request, "Tu compra ha sido confirmada")

        except Exception as e:
            print(e)
            messages.error(request, "No se ha podido realizar la compra, intenta nuevamente")

        return redirect(to="home")
    return render(request, 'app/shop/checkout.html', data)

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

def product_request(request):
    providers = Proveedor.objects.all()

    data = {
        'providers':providers
    }

    return render(request, 'app/employee/product_request.html', data)

def products_by_provider(request, id):
    provider = Proveedor.objects.get(id_proveedor=id)
    products = Producto.objects.filter(id_proveedor=id)
    productRequestFilter = ProductRequestFilter(request.GET, queryset=products)
    products = productRequestFilter.qs

    data = {
        'products':products,
        'productRequestFilter':productRequestFilter,
        'provider':provider
    }

    return render(request, 'app/employee/products_by_provider.html', data)

def order(request):
    orderProvider = cookieOrder(request)
    
    order = orderProvider['order']
    items = orderProvider['items']

    data = {
        'items':items, 
        'order':order
        }

    return render(request, 'app/employee/order.html', data)

# Aprobar datos de compra y delivery
def checkout_provider(request):
    profile = Persona.objects.get(usuario=request.user)

    tipoDoc = TipoDocumento.objects.all()

    cookie = cookieOrder(request)
    
    order = cookie['order']
    items = cookie['items']

    data = {
        'items':items, 
        'order':order,
        'tipoDoc':tipoDoc,
        }

    # Recibimos tipo documento y guardamos en bd la compra
    if request.method == 'POST':
        id_tipo_doc = request.POST.get('tipoDoc')
        subtotal = order['get_order_total']

        # iteramos el listado de productos y agregamos todos los proveedores pertenecientes al producto a un listado
        provider_list = []
        for i in items:
            provider = i['provider']
            provider_list.append(provider)

        # comprobamos que si el listado de proveedores no es único, retorne a la orden con mensaje de error
        if len(set(provider_list)) > 1:
            messages.error(request, "El listado sólo puede tener un tipo de proveedor, modifica el listado e intenta nuevamente")
            return redirect(to="order")

        
        provider = Proveedor.objects.get(nombre_empresa=provider_list[0])
        print(provider.id_proveedor)

        try:
            new_order = Orden.objects.create(
                fecha=datetime.datetime.now(), 
                total=subtotal, 
                # guardamos orden como tipo Proveedor
                id_tipo=TipoOrden.objects.get(id_tipo=2), 
                rut_persona=Persona.objects.get(rut_persona=profile),
                id_proveedor=Proveedor.objects.get(id_proveedor=provider.id_proveedor)
                )

            # loop de items en cookieCart
            for i in items:
                # instanciamos un producto desde el valor del carro de compra 
                producto = Producto.objects.get(id_producto=i['product']['id'])

                OrdenDetalle.objects.create(
                    id_producto = producto,
                    nro_orden = new_order,
                    cantidad = i['quantity'],
                    total = i['get_total']
                )

            # Datos para boleta/factura
            iva = 0
            # definir iva si es factura
            if id_tipo_doc == "2":
                iva = subtotal*0.19
            total = subtotal+iva

            recibo = Recibo.objects.create(
                fecha = datetime.datetime.now(),
                subtotal = total,
                iva = iva,
                total = total,
                id_tipo = TipoDocumento.objects.get(id_tipo=id_tipo_doc),
                nro_orden = new_order,
            )

            messages.success(request, "Tu orden ha sido generada")

        except Exception as e:
            print(e)
            messages.error(request, "No se ha podido realizar la compra, intenta nuevamente")

        return redirect(to="home")
    return render(request, 'app/employee/checkout.html', data)


