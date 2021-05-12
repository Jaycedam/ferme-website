import json
from .models import Producto

def cookieCart(request):

	#Create empty cart for now for non-logged in user
	try:
		cart = json.loads(request.COOKIES['cart'])
	except:
		cart = {}
		print('CART:', cart)

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