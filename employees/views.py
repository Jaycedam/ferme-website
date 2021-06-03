from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.admin.views.decorators import staff_member_required
from .filters import ProductAdminFilter
from .models import *
from .utils import cookieOrder
from .forms import *
from django.contrib import messages
import datetime

# Create your views here.
@staff_member_required
def home(request):

    orders = Orden.objects.filter(id_tipo=2)

    data = {
        'orders':orders
    }
    return render(request, 'employees/home.html', data)

@staff_member_required
def product_create(request):
    form = ProductForm()
    data = {
        "form":form
        }
    
    if request.method == 'POST':
        form = ProductForm(data=request.POST, files=request.FILES)

        if form.is_valid():
            form.save()
            messages.success(request, "Producto registrado correctamente")
            return redirect(to="product_management")

        data["form"] = form

    return render(request, 'employees/product/create.html', data)

@staff_member_required
def product_management(request):
    productos = Producto.objects.all()
    productosFiltered = ProductAdminFilter(request.GET, queryset=productos)
    productos = productosFiltered.qs

    data = {
        "productos":productos,
        "productosFiltered":productosFiltered
    }

    return render(request, 'employees/product/list.html', data)

@staff_member_required
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

    return render(request, 'employees/product/modify.html', data)

@staff_member_required
def product_request(request):
    providers = Proveedor.objects.all()

    data = {
        'providers':providers
    }

    return render(request, 'employees/order/product_request.html', data)

@staff_member_required
def products_by_provider(request, id):
    provider = Proveedor.objects.get(id_proveedor=id)
    products = Producto.objects.filter(id_proveedor=id)
    products_filtered = ProductAdminFilter(request.GET, queryset=products)
    products = products_filtered.qs

    data = {
        'products':products,
        'products_filtered':products_filtered,
        'provider':provider
    }

    return render(request, 'employees/order/products_by_provider.html', data)

@staff_member_required
def order(request):
    orderProvider = cookieOrder(request)
    
    order = orderProvider['order']
    items = orderProvider['items']

    data = {
        'items':items, 
        'order':order
        }

    return render(request, 'employees/order/order.html', data)

# Aprobar datos de compra y delivery
@staff_member_required
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
                id_proveedor=Proveedor.objects.get(id_proveedor=provider.id_proveedor),
                # asignamos orden como pendiente
                id_estado=Estado.objects.get(id_estado=1)
                )

            # loop de items en cookieCart
            for i in items:
                # instanciamos un producto desde el valor del carro de compra 
                producto = Producto.objects.get(id_producto=i['product']['id'])

                OrdenDetalle.objects.create(
                    id_producto = producto,
                    precio=producto.precio,
                    cantidad = i['quantity'],
                    total = i['get_total'],
                    nro_orden = new_order
                )

            messages.success(request, "Tu orden ha sido generada")

        except Exception as e:
            print(e)
            messages.error(request, "No se ha podido realizar la compra, intenta nuevamente")

        return redirect(to="employees_home")
    return render(request, 'employees/order/checkout.html', data)
