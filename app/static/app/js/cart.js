var updateBtns = document.getElementsByClassName('update-cart')

for(var i = 0; i < updateBtns.length; i++){
    updateBtns[i].addEventListener('click', function(){
        var id_producto = this.dataset.product
        var action = this.dataset.action
        console.log('id_producto:', id_producto, 'action:', action)

        addCookieItem(id_producto, action)
    })
}

function addCookieItem(id_producto, action){
	if (action == 'add'){
		if (cart[id_producto] == undefined){
		cart[id_producto] = {'quantity':1}

		}else{
			cart[id_producto]['quantity'] += 1
		}
	}

	if (action == 'remove'){
		cart[id_producto]['quantity'] -= 1

		if (cart[id_producto]['quantity'] <= 0){
			console.log('Item should be deleted')
			delete cart[id_producto];
		}
	}
	console.log('CART:', cart)
	document.cookie ='cart=' + JSON.stringify(cart) + ";domain=;path=/"

	location.reload()
	
}