import json
from .models import Producto

def cookieCart(request):
	try:
		cart = json.loads(request.COOKIES['cart'])
	except:
		cart = {}

	items = []
	order = {'get_cart_total':0}

	for i in cart:
		#We use try block to prevent items in cart that may have been removed from causing error
		try:
			product = Producto.objects.get(id_producto=i)
			total = (product.precio * cart[i]['quantity'])

			order['get_cart_total'] += total

			item = {
				'product':{
					'id':product.id_producto,
					'name':product.producto, 
					'price':product.precio
					}, 
				'quantity':cart[i]['quantity'],
				'get_total':total,
				}
			items.append(item)
		except:
			pass
			
	return {'order':order, 'items':items}

def cookieOrder(request):
	try:
		orderCookie = json.loads(request.COOKIES['order'])
	except:
		orderCookie = {}

	items = []
	order = {'get_order_total':0}

	for i in orderCookie:
		#We use try block to prevent items in order that may have been removed from causing error
		try:
			product = Producto.objects.get(id_producto=i)
			total = (product.precio_proveedor * orderCookie[i]['quantity'])

			order['get_order_total'] += total

			item = {
				'product':{
					'id':product.id_producto,
					'name':product.producto, 
					'price':product.precio_proveedor
					}, 
				'provider':product.id_proveedor,
				'quantity':orderCookie[i]['quantity'],
				'get_total':total,
				}
			items.append(item)
		except Exception as e:
			print(e)
			
	return {'order':order, 'items':items}