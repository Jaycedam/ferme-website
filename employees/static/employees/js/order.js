var updateBtns = document.getElementsByClassName('update-order')

for(var i = 0; i < updateBtns.length; i++){
    updateBtns[i].addEventListener('click', function(){
        var id_producto = this.dataset.product
        var action = this.dataset.action
        console.log('id_producto:', id_producto, 'action:', action)

        addOrderItem(id_producto, action)
    })
}

function addOrderItem(id_producto, action){
	if (action == 'add'){
		if (order[id_producto] == undefined){
			order[id_producto] = {'quantity':1}

		Swal.fire({
			icon: 'success',
			title: 'Producto agregado',
			text: '¿Quieres generar la orden de compra?',
			showCancelButton: true,
			confirmButtonText: 'Generar orden <i class="bi bi-file-earmark-text"></i>',
			confirmButtonColor: '#0b5ed7',
			cancelButtonText: 'Agregar más productos',
			reverseButtons: true,
			}).then((result) => {
			if (result.isConfirmed) {
				location.href="/employees/order"
			} 

		})

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

	if (action == 'delete'){
		delete order[id_producto];
		location.reload()
	}

	console.log('order:', order)
	document.cookie = 'order=' + JSON.stringify(order) + ";domain=;path=/;SameSite=Lax"

}

function deleteOrder(){
	document.cookie = 'order=' + null + ";domain=;path=/;SameSite=Lax"
}