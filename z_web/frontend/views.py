from django.contrib.admin.views.decorators import staff_member_required

from django.shortcuts import render_to_response
from django.template import RequestContext

from parametros.models import Periodo
from .stats import get_utlizacion_equipo


@staff_member_required
def index(request):
    context = {}
    periodos = Periodo.objects.all().order_by('-fecha_inicio')
    context["periodos"] = periodos
    if 'periodo' in request.GET:
        context["equipos"], context["totales"] = get_utlizacion_equipo(Periodo.objects.get(
            pk=request.GET["periodo"]))
    else:
        context["equipos"], context["totales"] = get_utlizacion_equipo(periodos[0])

    return render_to_response("frontend/estadistica.html",
                              context,
                              context_instance=RequestContext(request))

#
# class EstadisticaView(TemplateView):
#     template_name = "frontend/estadistica.html"
#
#     def dispatch(self, request, *args, **kwargs):
#         return super(EstadisticaView, self).dispatch(request, *args, **kwargs)
#
#     def get_context_data(self, **kwargs):
#         context = super(EstadisticaView, self).get_context_data(**kwargs)
#         periodos = Periodo.objects.all().order_by('-fecha_inicio')
#         context["periodos"] = periodos
#         if 'periodo' in self.request.GET:
#             context["equipos"] = self.get_utlizacion_equipo(Periodo.objects.get(pk=self.request.GET["periodo"]))
#         else:
#             context["equipos"] = self.get_utlizacion_equipo(periodos[0])
#
#         return context











    """ Agrupar por obra!      processed = defaultdict(lambda: defaultdict(lambda: defaultdict(dict)))"""

"""
    String query= "SELECT EQ.N_INTERNO as nint, f.nombre as familia, O.NOMBRE as nombre, "
+                + "COUNT(PD.id) as DiasEnMes, OB.OBRA as obra, OB.id as obraid "
+                + "FROM partediario PD "
+                + "INNER JOIN operarios O ON PD.operario = O.id "
+                + "INNER JOIN obras OB ON PD.obra = OB.id "
+                + "INNER JOIN registro_equipo RQ ON PD.equipo = RQ.id "
+                + "INNER JOIN equipos EQ ON RQ.equipo = EQ.id "
+                + "INNER JOIN familia_equipo f ON f.id = EQ.familia_equipo_id "
+                + "where PD.fecha <= '"+ FechaUtil.getFechaSQL(hasta)+"' and "
+                + "PD.fecha >= '"+ FechaUtil.getFechaSQL(desde)+"' and EQ.id != 1 "
+                + "AND PD.situacion =1 "
+                + "group by OB.id, EQ.N_INTERNO "
+                + "order by OB.id, EQ.N_INTERNO desc";

"""