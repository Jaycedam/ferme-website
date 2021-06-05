from .models import Recibo, OrdenDetalle, Orden, Persona
import os

from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.contrib.staticfiles import finders
from django.template import Context, Template


def extract_request_variables(request, id):

    page_size = request.POST.get('page_size', 'letter')
    page_orientation = request.POST.get('page_orientation', 'portrait')

    pagesize = "%s %s" % (
        page_size, page_orientation
    )

    template = Template(request.POST.get('data', ''))
    data = template.render(Context({}))

    invoice = Recibo.objects.get(nro_orden=id)
    order = Orden.objects.get(nro_orden=id)
    items = OrdenDetalle.objects.filter(nro_orden=id)

    return {
        'invoice':invoice,
        'order':order,
        'items':items,
        'pagesize': pagesize,
        'data': data,
        'page_orientation': page_orientation,
        'page_size': page_size,
        'example_number': request.POST.get("example_number", '1'),
        'border': request.POST.get('border', '')
    }

def render_pdf(request, id):
    template_path = 'orders/invoice.html'
    context = extract_request_variables(request, id)

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="report.pdf"'

    template = get_template(template_path)
    html = template.render(context)
    if request.POST.get('show_html', ''):
        response['Content-Type'] = 'application/text'
        response['Content-Disposition'] = 'attachment; filename="report.txt"'
        response.write(html)
    else:
        pisaStatus = pisa.CreatePDF(
            html, dest=response)
        if pisaStatus.err:
            return HttpResponse('We had some errors with code %s <pre>%s</pre>' % (pisaStatus.err,
                                                                                   html))
    return response