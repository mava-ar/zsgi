from collections import defaultdict

from django.db.models import Count

from registro.models import Partediario
from costos.models import LubricanteFluidosHidro, TrenRodaje, CostoPosesion, ReserveReparaciones, CostoParametro
from zweb_utils.format import decimal_format


def get_calculo_costo(costos, valores, horas_dia, total=0):
    val = costos.get(valores["equipo__equipo__familia_equipo_id"], 0) * horas_dia * valores["dias_mes"]
    total += val
    return total, decimal_format(val)


def get_utlizacion_equipo(periodo):
    qs = Partediario.objects.filter(
        fecha__lte=periodo.fecha_fin, fecha__gte=periodo.fecha_inicio, situacion__id=1).exclude(
        equipo__equipo_id=1).exclude(equipo_id__isnull=True).values(
        'equipo__equipo_id', 'equipo__equipo__n_interno', 'funcion__funcion', 'operario__nombre',
        'obra__obra', 'obra_id', 'equipo__equipo__familia_equipo_id').annotate(dias_mes=Count('id')).order_by(
        'obra_id', '-equipo__equipo__n_interno')

    processed = defaultdict(list)
    for result in qs:
        processed[result["obra__obra"]].append(result)
    result = dict(processed.items())
    ids = list(set(x["equipo__equipo__familia_equipo_id"] for x in qs))
    param = CostoParametro.vigentes.get_vigente_el_periodo(periodo).first()
    # calculo de lubricantes
    lubris = dict(LubricanteFluidosHidro.objects.filter(
        periodo=periodo, familia_equipo_id__in=ids).values_list('familia_equipo', 'monto_hora'))
    # calculo de tren
    tren = dict(TrenRodaje.objects.filter(periodo=periodo, familia_equipo_id__in=ids).values_list('familia_equipo', 'monto_hora'))
    # calculo de posesion
    posesion = dict(CostoPosesion.objects.filter(periodo=periodo, familia_equipo_id__in=ids).values_list('familia_equipo', 'monto_hora'))
    # calculo de reparacion
    repara = dict(ReserveReparaciones.objects.filter(periodo=periodo, familia_equipo_id__in=ids).values_list('familia_equipo', 'monto_hora'))
    totales = dict()
    for k, v in result.items():
        total = 0
        for l in v:
            total, l["fluido"] = get_calculo_costo(lubris, l, param.dias_mes, total)  # lubris.get(l["equipo__equipo__familia_equipo_id"], 0) * param.horas_dia * l["dias_mes"]
            total, l["tren"] = get_calculo_costo(tren, l, param.dias_mes, total)  # tren.get(l["equipo__equipo__familia_equipo_id"], 0) * param.horas_dia * l["dias_mes"]
            total, l["posesion"] = get_calculo_costo(posesion, l, param.dias_mes, total)  # posesion.get(l["equipo__equipo__familia_equipo_id"], 0) * param.horas_dia * l["dias_mes"]
            total, l["repara"] = get_calculo_costo(repara, l, param.dias_mes, total)  # repara.get(l["equipo__equipo__familia_equipo_id"], 0) * param.horas_dia * l["dias_mes"]
        totales[k] = decimal_format(total)

    return result, totales
