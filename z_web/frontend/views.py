from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import messages
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.utils.safestring import mark_safe

from parametros.models import Periodo
from costos.models import CostoParametro
from .stats import get_utlizacion_equipo, get_cc_on_periodo, get_ventas_costos


@staff_member_required
def index(request):
    context = {}
    periodos = Periodo.objects.all().order_by('-fecha_inicio')
    context["periodos"] = periodos
    if periodos:
        if 'periodo' in request.GET:
            periodo = Periodo.objects.get(pk=request.GET["periodo"])
        else:
            periodo = periodos[0] if periodos else None
        context["periodo"] = periodo
        try:
            context["equipos"], context["totales"] = get_utlizacion_equipo(periodo)
            context["resumen_costos"], context["total"], totales_costos = get_cc_on_periodo(periodo, context["totales"])
        except CostoParametro.DoesNotExist as e:
            messages.add_message(request, messages.WARNING,
                                 mark_safe("No están definidos los <a href='/costos/costoparametro'>parámetros de costos</a> para el "
                                           "periodo {}".format(periodo)))
        try:
            context["cert_costos"], context["costos_ventas_total"] = get_ventas_costos(periodo, totales_costos)
        except Exception:
            pass
    else:
        messages.add_message(request, messages.WARNING, "No hay periodos definidos en el sistema.")
    return render_to_response("frontend/panel_control.html",
                              context,
                              context_instance=RequestContext(request))
