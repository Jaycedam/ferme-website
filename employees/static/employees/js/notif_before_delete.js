$(document).ready(function () {
    $('form #btn-delete').click(function (e) {
        let $form = $(this).closest('form');

        Swal.fire({
            icon: 'warning',
            title: '¿Estás seguro que deseas eliminar esta orden?',
            text: 'Esta acción no se puede deshacer',
            showCancelButton: true,
            confirmButtonText: 'Eliminar',
            confirmButtonColor: '#d90000',
            cancelButtonText: 'Cancelar',
            cancelButtonColor: '#696969',
            reverseButtons: true,
            }).then((result) => {
            if (result.isConfirmed) {
                $form.submit()
            } 
        })
    })
});
