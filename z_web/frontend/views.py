from django.contrib.admin.views.decorators import staff_member_required

from django.shortcuts import render_to_response
from django.template import RequestContext

from parametros.models import Periodo
from .stats import get_utlizacion_equipo, get_cc_on_periodo


@staff_member_required
def index(request):
    context = {}
    periodos = Periodo.objects.all().order_by('-fecha_inicio')
    context["periodos"] = periodos
    if 'periodo' in request.GET:
        periodo = Periodo.objects.get(pk=request.GET["periodo"])
    else:
        periodo = periodos[0]
    context["periodo"] = periodo
    context["equipos"], context["totales"] = get_utlizacion_equipo(periodo)
    context["resumen_costos"], context["total"] = get_cc_on_periodo(periodo, context["totales"])
    return render_to_response("frontend/estadistica.html",
                              context,
                              context_instance=RequestContext(request))



