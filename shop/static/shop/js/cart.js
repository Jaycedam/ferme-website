var updateBtns = document.getElementsByClassName('update-cart')

for(var i = 0; i < updateBtns.length; i++){
    updateBtns[i].addEventListener('click', function(){
        var id_producto = this.dataset.product;
        var action = this.dataset.action;
        addCartItem(id_producto, action);
    })
}

function addCartItem(id_producto, action){
	if (action == 'add'){
		if (cart[id_producto] == undefined){
		cart[id_producto] = {'quantity':1}

		Swal.fire({
			icon: 'success',
			title: 'Producto agregado',
			text: '¿Quieres ir al carro de compras?',
			showCancelButton: true,
			confirmButtonText: 'Ir al carro <i class="bi bi-cart"></i>',
			cancelButtonText: 'Seguir comprando',
			confirmButtonColor: '#0b5ed7',
			reverseButtons: true,
		  }).then((result) => {
			if (result.isConfirmed) {
			  location.href="/cart"
			} 
		  })

		}else{
			cart[id_producto]['quantity'] += 1
			location.reload()
		}
	}

	if (action == 'remove'){
		cart[id_producto]['quantity'] -= 1

		if (cart[id_producto]['quantity'] <= 0){
			console.log('Item should be deleted')
			delete cart[id_producto];
		}
		location.reload()
	}
	console.log('CART:', cart)
	document.cookie = 'cart=' + JSON.stringify(cart) + ";domain=;path=/;SameSite=Lax"
}