from shop.models import Delivery, OrdenDetalle
from django import template
from django.core.mail.message import EmailMultiAlternatives
from django.shortcuts import render
from django.template.loader import get_template
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
def send_order_email(mail, order):
    items = OrdenDetalle.objects.filter(nro_orden=order)
    delivery = Delivery.objects.get(nro_orden=order)
    data = {
        'mail':mail,
        'order':order,
        'items':items,
        'delivery':delivery
    }

    template = get_template('email_sender/email.html')
    content = template.render(data)

    email = EmailMultiAlternatives(
        'Orden de compra - Ferme Services',
        'Adjuntamos el detalle de tu orden',
        settings.EMAIL_HOST_USER,
        [mail]
    )

    email.attach_alternative(content, 'text/html')
    email.send()

