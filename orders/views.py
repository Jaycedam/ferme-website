from shop.models import Delivery, Motivo, NcDetalle, NotaCredito, Producto
from django.shortcuts import render, redirect
from .models import *
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .filters import OrderToProviderFilter, OrdersFilter, NotaCreditoFilter
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
    delivery = Delivery.objects.get(nro_orden=order)

    data = {
        'order':order,
        'order_items':order_items,
        'status':status,
        'delivery':delivery,
    }

    
    if NotaCredito.objects.filter(nro_orden=order).exists():
        nc = NotaCredito.objects.filter(nro_orden=order)
        nc_items = []
        for i in nc:
            items = NcDetalle.objects.filter(nro_nota_credito=i)
            for e in items:    
                nc_items.append(e)

        data['nc'] = nc
        data['nc_items'] = nc_items
        print(nc_items)
    
    # instanciamos recibo si existe
    try: 
        data['recibo'] = Recibo.objects.get(nro_orden=id)
    except:
        pass

    return render(request, 'orders/customer/order.html', data)

# cancelar orden por cliente
@login_required
def cancel_order(request, id):
    order = Orden.objects.get(nro_orden=id)
    order_items = OrdenDetalle.objects.filter(nro_orden=order)
    profile = Persona.objects.get(usuario=request.user)
    motives = Motivo.objects.all()

    # si la orden no pertenece al usuario actual, se redirige al home
    if order.rut_persona != profile:
        return redirect(to='home')

    data = {
        'order':order,
        'order_items':order_items,
        'motives':motives
    }

    # si existe una cancelacion, la guardamos 
    try:
        nc = NotaCredito.objects.filter(nro_orden=order)
        item_requests = []

        for i in nc:
            details = NcDetalle.objects.filter(nro_nota_credito=i).values('id_producto')
            for e in details:
                item_requests.append(str(e['id_producto']))
      
        data['item_requests']=item_requests

    except Exception as e:
        print(e)

    if request.method == 'POST':
        items = request.POST.getlist('items')
        descripcion = request.POST.get('desc')
        motivo = request.POST.get('motive')

        if items == []:
            messages.error(request, "Debes seleccionar productos a cancelar")

        if items != []:
            # iteramos los productos seleccionados
            for i in items:
                # vemos si i existe dentro del listado de cancelaciones ya realizadas, si existe redirige y no continua
                if i in item_requests:
                    messages.error(request, "Ya existe una solicitud para uno de los productos seleccionados")
                    return redirect(to="orders")

            try:
                total = 0
                nc = NotaCredito.objects.create(
                    fecha = datetime.datetime.now(),
                    total = total,
                    descripcion = descripcion,
                    id_estado = Estado.objects.get(id_estado=1),
                    id_motivo = Motivo.objects.get(id_motivo=motivo),
                    nro_orden = order
                )

                # iteracion del listado completo de productos de la orden
                for i in order_items:
                    # pasamos los productos seleccionados a un listado de objetos
                    products = Producto.objects.filter(id_producto__in=(items))
                    # verificamos si i existe dentro del listado para crear el detalle
                    if i.id_producto in products:
                        total += i.total
                        NcDetalle.objects.create(
                                id_producto = i.id_producto,
                                precio = i.precio,
                                cantidad = i.cantidad,
                                total = i.total,
                                nro_nota_credito = nc
                            )
                
                # actualizamos el total de la nc 
                # con la suma de los productos seleccionados
                nc.total = total
                nc.save()
        
                messages.success(request, "Solicitud de anulación enviada")
                return redirect(to=orders)


            except Exception as e:
                print(e)    
           
    return render(request, 'orders/customer/cancel_order.html', data)

# ver listado de solicitudes de cancelacion asociadas al usuario actual
@login_required
def cancel_requests(request):
    profile = Persona.objects.get(usuario=request.user)

    filter = NotaCreditoFilter(request.GET, queryset=NotaCredito.objects.filter(nro_orden__rut_persona=profile))
    cancel_requests = filter.qs

    paginator = Paginator(cancel_requests, 20)
    page_number = request.GET.get('page', 1)
    page = paginator.get_page(page_number)

    data = {
        'entity':page,
        'filter':filter
    }
    return render(request, 'orders/customer/cancel_requests.html', data)

# ver detalle de solicitud del usuario actual
@login_required
def cancel_request(request, id):

    nc = NotaCredito.objects.get(nro_nota_credito=id)
    items = NcDetalle.objects.filter(nro_nota_credito=nc)

    # si la nc no pertenece al usuario actual, redirige al home
    if nc.nro_orden.rut_persona != Persona.objects.get(usuario=request.user):
        return redirect(to='home')
    
    data = {
        'nc':nc,
        'items':items
    }

    return render(request, 'orders/customer/cancel_request.html', data)


############################### EMPLEADO ###############################
# listado de todas las solicitudes de cancelacion (empleado)
@staff_member_required
def manage_cancel_orders(request):
    filter = NotaCreditoFilter(request.GET, queryset=NotaCredito.objects.all())
    cancel_requests = filter.qs

    paginator = Paginator(cancel_requests, 20)
    page_number = request.GET.get('page', 1)
    page = paginator.get_page(page_number)

    data = {
        'entity':page,
        'filter':filter
    }    
    
    return render(request, 'orders/employee/cancel_requests.html', data)

# detalle de cancelacion con opc de cambiar estado (empleado)
@staff_member_required
def manage_cancel_order(request, id):
    nc = NotaCredito.objects.get(nro_nota_credito=id)
    items = NcDetalle.objects.filter(nro_nota_credito=nc)
    status = Estado.objects.all()
    pendiente = status[0]
    
    data = {
        'nc':nc,
        'items':items,
        'status':status,
        'pendiente':pendiente
    }

    if request.method == "POST":
        status_selected = request.POST.get('status')
        nc.id_estado = Estado.objects.get(id_estado=status_selected)
        nc.save()
        if status_selected == "2":
            order = Orden.objects.get(nro_orden=nc.nro_orden.get_id())

        messages.success(request, f"El estado de la solicitud {nc.nro_nota_credito} ha sido actualizado")
        return redirect(to='manage_cancel_orders')

    return render(request, 'orders/employee/cancel_request.html', data)


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
        'ordersFiltered':ordersFiltered,
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
        'pendiente':Estado.objects.get(id_estado=1)
    }
    
    # instanciamos recibo si existe
    try: 
        data['recibo'] = Recibo.objects.get(nro_orden=id)
    except:
        pass

    if request.method == 'POST':
        order_items.delete()
        order.delete()
        messages.success(request, "Orden eliminada correctamente")
        return redirect(to='orders_to_provider')

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

