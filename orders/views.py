from django.shortcuts import render, redirect
from .models import *
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .filters import OrderToProviderFilter, OrdersFilter
import datetime
from django.core.paginator import Paginator

# Create your views here.
############################### CLIENTE ###############################
# listado de ordenes general
@login_required
def orders(request):
    user = request.user
    data = {}
    try:
        profile = Persona.objects.get(usuario=user)

        orders_filtered = OrdersFilter(request.GET, queryset=Orden.objects.filter(rut_persona=profile, id_tipo=1))
        orders = orders_filtered.qs

        paginator = Paginator(orders, 20)
        page_number = request.GET.get('page', 1)
        page = paginator.get_page(page_number)

        data['entity'] = page
        data['orders_filtered'] = orders_filtered
        
    except Exception as e:
        print(e)

    return render(request, 'orders/customer/orders.html', data)

# detalles de una orden general
@login_required
def order(request, id):
    order = Orden.objects.get(nro_orden=id)
    order_items = OrdenDetalle.objects.filter(nro_orden=id)
    status = Estado.objects.all()

    data = {
        'order':order,
        'order_items':order_items,
        'status':status,
    }
    
    # instanciamos recibo si existe
    try: 
        data['recibo'] = Recibo.objects.get(nro_orden=id)
    except:
        pass

    return render(request, 'orders/customer/order.html', data)


############################### EMPLEADO ###############################
# listado de ordenes hacia proveedor
@staff_member_required
def orders_to_provider(request):
    ordersFiltered = OrderToProviderFilter(request.GET, queryset=Orden.objects.filter(id_tipo=2))
    orders = ordersFiltered.qs

    paginator = Paginator(orders, 20)
    page_number = request.GET.get('page', 1)
    page = paginator.get_page(page_number)

    data = {
        'entity':page,
        'ordersFiltered':ordersFiltered
    }
    return render(request, 'orders/employee/orders_to_provider.html', data)


# detalles de una orden hacia un proveedor
@staff_member_required
def order_provider(request, id):
    order = Orden.objects.get(nro_orden=id)
    order_items = OrdenDetalle.objects.filter(nro_orden=id)

    data = {
        'order':order,
        'order_items':order_items,
    }
    
    # instanciamos recibo si existe
    try: 
        data['recibo'] = Recibo.objects.get(nro_orden=id)
    except:
        pass

    return render(request, 'orders/employee/order_provider.html', data)


############################### PROVEEDOR ###############################
# listado de ordenes asociadas al proveedor actual 
@login_required
def order_requests(request):
    data = {}
    try:
        provider = Proveedor.objects.get(rut_persona=Persona.objects.get(usuario=request.user))
        orders_filtered = OrdersFilter(request.GET, queryset=Orden.objects.filter(id_proveedor=provider))
        orders = orders_filtered.qs

        paginator = Paginator(orders, 20)
        page_number = request.GET.get('page', 1)
        page = paginator.get_page(page_number)

        data ={
            'entity':page,
            'orders_filtered':orders_filtered
        }

    except:
        pass
        
    return render(request, 'orders/provider/orders.html', data)


# detalles de orden asociada a proveedor actual
@login_required # agregar validacion que la orden pertenezca al usuario actual
def order_request(request, id):
    order = Orden.objects.get(nro_orden=id)
    order_items = OrdenDetalle.objects.filter(nro_orden=id)
    status = Estado.objects.all()

    # variable que se usará para validar solo ordenes pendientes
    undefined = status.get(id_estado=1)
   
    data = {
        'order':order,
        'order_items':order_items,
        'status':status,
        'undefined':undefined
    }    
    
    # obtenemos datos del proveedor si existe
    try:
        profile = Persona.objects.get(usuario=request.user)
        provider = Proveedor.objects.get(rut_persona=profile)
        # si el proveedor actual es el mismo que la orden, se manda el proveedor por data
        if order.id_proveedor == provider:
            data['provider'] = provider
    except Exception as e:
        print(e)
        pass

    if request.method == 'POST':
        try:
            status = request.POST.get('status')
            # si es aprobado, se crea factura
            if status == "2":
                iva = round(order.total*0.19)
                subtotal = order.total - iva
                total = subtotal + iva

                Recibo.objects.create(
                    fecha = datetime.datetime.now(),
                    subtotal = subtotal,
                    iva = iva,
                    total = total,
                    # tipo factura
                    id_tipo = TipoDocumento.objects.get(id_tipo=2),
                    nro_orden =  Orden.objects.get(nro_orden=order.nro_orden),
                )
            
            #actualizamos el estado al seleccionado en el form y guardamos
            order.id_estado = Estado.objects.get(id_estado=status) 
            order.save() 

            messages.success(request, "Estado modificado correctamente")
            return redirect(to="order_requests")

        except Exception as e:
            messages.error(request, "No se ha podido actualizar el estado")
            print(e)

    return render(request, 'orders/provider/order.html', data)
