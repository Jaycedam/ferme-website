import json
from .models import Producto

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
			order['get_order_total'] += round(order['get_order_total'] * 0.19)

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