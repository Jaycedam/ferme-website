var updateBtns = document.getElementsByClassName('update-order')

for(var i = 0; i < updateBtns.length; i++){
    updateBtns[i].addEventListener('click', function(){
        var id_producto = this.dataset.product
        var id_proveedor = this.dataset.provider
        var action = this.dataset.action
        console.log('id_producto:', id_producto, 'id_provider:', id_proveedor, 'action:', action)

        addCookieItem(id_producto, id_proveedor, action)
    })
}

function addCookieItem(id_producto, id_proveedor, action){
	if (action == 'add'){
		if (order[id_producto] == undefined){
		order[id_producto] = {'quantity':1, 'id_proveedor':id_proveedor}
		Swal.fire(
			'Felicitaciones',
			'Producto agregado correctamente',
			'success'
		)
		}else{
			order[id_producto]['quantity'] += 1
			location.reload()
		}
	}

	if (action == 'remove'){
		order[id_producto]['quantity'] -= 1

		if (order[id_producto]['quantity'] <= 0){
			console.log('Item should be deleted')
			delete order[id_producto];
		}
		location.reload()
	}
	console.log('order:', order)
	document.cookie ='order=' + JSON.stringify(order) + ";domain=;path=/"
}

function deleteOrder(){
    document.cookie = 'order=' + null + ";domain=;path=/"
}