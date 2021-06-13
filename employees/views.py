from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.admin.views.decorators import staff_member_required
from .filters import ProductAdminFilter
from .models import *
from .utils import cookieOrder
from .forms import *
from django.contrib import messages
import datetime
from django.core.paginator import Paginator
from django.db.models import Sum, Count, Max

# Create your views here.
@staff_member_required
def home(request):
    orders = Orden.objects.filter(id_tipo=2)

    # estadísticas de top 10 productos mas vendidos
    product_stat_sales = Producto.objects.annotate(sales=Sum('ordendetalle__cantidad')).order_by('sales')[:5]
    product_stat_sales_labels = []
    product_stat_sales_data = []
    for i in product_stat_sales:
        # se agregan los labels y data a una lista separada para mostrar en el frontend como chart
        product_stat_sales_labels.append(i.producto)
        product_stat_sales_data.append(int(i.sales))

    # estadísticas de usuarios
    user_stats_labels = []
    user_stats_data = []

    active_users = User.objects.count()
    user_stats_labels.append("Total usuarios registrados")
    user_stats_data.append(active_users)

    today = datetime.date.today() + datetime.timedelta(days=1)
    last_week = datetime.date.today() - datetime.timedelta(days=7)
    last_month = datetime.date.today() - datetime.timedelta(days=30)

    monthly_users = User.objects.filter(last_login__range=(last_week, today)).count()
    user_stats_labels.append("Usarios activos (30 días)")
    user_stats_data.append(monthly_users)

    weekly_users = User.objects.filter(last_login__range=(last_week, today)).count()
    user_stats_labels.append("Usarios activos (7 días)")
    user_stats_data.append(weekly_users)

    # estadísticas de fechas de venta
    order_stats_data = []
    last_year_orders_data = []

    orders = Orden.objects.filter(id_tipo=1, id_estado=2, fecha__year=today.year)
    last_year_orders = Orden.objects.filter(id_tipo=1, id_estado=2, fecha__year=today.year-1)

    # iteracion por 12 meses donde se filtra por mes y se cuentan las ordenes realizadas por mes/año
    for i in range(12):
        orders_by_month = orders.filter(fecha__month=i+1).count()
        last_year_orders_by_month = last_year_orders.filter(fecha__month=i+1).count()
        order_stats_data.append(orders_by_month)
        last_year_orders_data.append(last_year_orders_by_month)

    data = {
        'orders':orders,
        'product_stat_sales_labels':product_stat_sales_labels,
        'product_stat_sales_data':product_stat_sales_data,
        'user_stats_labels':user_stats_labels,
        'user_stats_data':user_stats_data,
        'order_stats_data':order_stats_data,
        'last_year_orders_data':last_year_orders_data
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
    products_filtered = ProductAdminFilter(request.GET, queryset=Producto.objects.all())
    products = products_filtered.qs
    
    paginator = Paginator(products, 20)
    page_number = request.GET.get('page', 1)
    page = paginator.get_page(page_number)

    data = {
        "entity":page,
        "products_filtered":products_filtered
    }

    return render(request, 'employees/product/list.html', data)

@staff_member_required
def product_modify(request, id):
    product = get_object_or_404(Producto, id_producto=id)

    data = {
        'form':ProductModifyForm(instance=product)
    }

    if request.method == 'POST':
        form = ProductModifyForm(data=request.POST, instance=product, files=request.FILES)

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
    products_filtered = ProductAdminFilter(request.GET, queryset=Producto.objects.filter(id_proveedor=id))
    products = products_filtered.qs

    paginator = Paginator(products, 20)
    page_number = request.GET.get('page', 1)
    page = paginator.get_page(page_number)

    data = {
        'entity':page,
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

    if Persona.objects.filter(usuario=request.user).exists():
        data['profile'] = Persona.objects.get(usuario=request.user)


    return render(request, 'employees/order/order.html', data)

# Aprobar datos de compra y delivery
@staff_member_required
def checkout_provider(request):
    tipoDoc = TipoDocumento.objects.all()

    cookie = cookieOrder(request)
    
    order = cookie['order']
    items = cookie['items']

    data = {
        'items':items, 
        'order':order,
        'tipoDoc':tipoDoc,
        }
    
    if Persona.objects.filter(usuario=request.user).exists():
        profile = Persona.objects.get(usuario=request.user)
        data['profile'] = profile


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
            if new_order:
                new_order.id_estado = Estado.objects.get(id_estado=3)
                new_order.save()
            print(e)
            messages.error(request, "No se ha podido realizar la compra, intenta nuevamente")

        return redirect(to="employees_home")
    return render(request, 'employees/order/checkout.html', data)
