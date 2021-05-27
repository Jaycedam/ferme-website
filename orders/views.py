from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages

# Create your views here.

def orders(request):
    user = request.user

    data = {}
    try:
        profile = Persona.objects.get(usuario=user)

        data['orders'] = Orden.objects.filter(rut_persona=profile, id_tipo=1)
        
        if Proveedor.objects.filter(rut_persona=profile).exists():
            provider = Proveedor.objects.get(rut_persona=profile)
            data['order_provider'] = Orden.objects.filter(id_proveedor=provider)
    except Exception as e:
        print(e)

    return render(request, 'orders/orders.html', data)

def order(request, id):
    doc = Recibo.objects.get(nro_orden=id)
    order = Orden.objects.get(nro_orden=id)
    order_items = OrdenDetalle.objects.filter(nro_orden=id)
    status = Estado.objects.all()

    data = {
        'doc':doc,
        'order':order,
        'order_items':order_items,
        'status':status,
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
            # actualizamos el estado al seleccionado en el form y guardamos
            order.id_estado =  Estado.objects.get(id_estado=request.POST.get('status')) 
            order.save()
            
            messages.success(request, "Estado modificado correctamente")
            return redirect(to="orders")

        except Exception as e:
            messages.error(request, "No se ha podido actualizar el estado")
            print(e)
        

    return render(request, 'orders/order.html', data)