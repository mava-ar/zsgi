from collections import defaultdict

from django.db.models import Count, When, Case, Sum

from costos.models import (LubricanteFluidosHidro, TrenRodaje, CostoPosesion, ReserveReparaciones, CostoParametro,
                           CostoManoObra, CostoSubContrato, MaterialesTotal, ServicioPrestadoUN)
from core.models import Obras
from registro.models import Partediario, Certificacion


def get_calculo_costo(costos, valores, horas_dia, total=0):
    val = costos.get(valores["registro_equipo__equipo__familia_equipo_id"], 0) * horas_dia * valores["dias_mes"]
    total += val
    return total, val


def calcular_item_costo(report, datos, no_prorrat, prorrat=[], multiplicador=1):
    lista = []

    for x in no_prorrat:
        lista.append(datos.get(x, 0) * multiplicador if datos.get(x, 0) else 0)
    report.append(lista)

    if prorrat:
        lista_prorrat = []
        total_prorrateo = 0
        for x in prorrat:
            data = datos.get(x, 0)
            if data:
                total_prorrateo += (data * multiplicador)
        total_prorrateo /= len(no_prorrat)
        for x in no_prorrat:
            lista_prorrat.append(total_prorrateo)
        report.append(lista_prorrat)
    return report


def get_utlizacion_equipo(periodo):
    qs = Partediario.objects.filter(
        fecha__lte=periodo.fecha_fin, fecha__gte=periodo.fecha_inicio, situacion__id=1).exclude(
        registro_equipo__equipo_id=1).exclude(registro_equipo__isnull=True).values(
        'registro_equipo__equipo_id', 'registro_equipo__equipo__n_interno', 'funcion__funcion', 'operario__nombre',
        'obra__obra', 'obra_id', 'registro_equipo__equipo__familia_equipo_id').annotate(dias_mes=Count('id')).order_by(
        '-obra_id', '-registro_equipo__equipo__n_interno')

    processed = defaultdict(list)
    for result in qs:
        processed[result["obra__obra"]].append(result)
    result = dict(processed.items())
    ids = list(set(x["registro_equipo__equipo__familia_equipo_id"] for x in qs))
    param = CostoParametro.objects.get(periodo=periodo)
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
            total, l["fluido"] = get_calculo_costo(lubris, l, param.dias_mes, total)
            total, l["tren"] = get_calculo_costo(tren, l, param.dias_mes, total)
            total, l["posesion"] = get_calculo_costo(posesion, l, param.dias_mes, total)
            total, l["repara"] = get_calculo_costo(repara, l, param.dias_mes, total)
        totales[v[0]["obra_id"]] = total

    return result, totales


def get_cc_on_periodo(periodo, totales):
    param = CostoParametro.objects.get(periodo=periodo)
    # Todas las obras implicadas en costos
    ccs = Obras.objects.filter(es_cc=True).values_list('id', 'codigo', 'prorratea_combustible',
                                                       'prorratea_manoobra', 'prorratea_materiales').order_by("pk")
    # Ids de obras tipo CC (con costos prorrateables y sin)
    obras_ids = [x[0] for x in ccs]
    pro_combustible = [x[0] for x in ccs if x[2]]
    pro_manoobra = [x[0] for x in ccs if x[3]]
    pro_materiales = [x[0] for x in ccs if x[4]]

    # Busco las cabeceras (CC no prorrateable)
    no_prorrat = dict(ccs.filter(prorratea_combustible=False,
                                 prorratea_manoobra=False,
                                 prorratea_materiales=False).values_list('id', 'codigo').order_by('pk'))

    # Defino el head del reporte

    headers = [x for x in no_prorrat.values()]
    headers.insert(0, "TIPO DE COSTO")
    tipo_costo_headers = ["Combustible", "Prorrateo de Combustible", "Mano de Obra", "Prorrateo de Mano de Obra", "Subcontratos" ,
     "Utilización de equipos", "Materiales", "Prorateo de Materiales", "Totales"]

    # report.append(headers)

    values = []
    # combustible
    combustible = dict(ccs.annotate(combustible=Sum(
        Case(
            When(
                partediario__fecha__gte=periodo.fecha_inicio,
                partediario__fecha__lte=periodo.fecha_fin,
                then='partediario__registro_equipo__cant_combustible')
        )
    )
    ).values_list('id', 'combustible'))


    # Prorrateo de combustible
    values = calcular_item_costo(
        values,
        combustible,
        no_prorrat,
        pro_combustible, multiplicador=param.precio_go)

    # Mano de obra
    mos = dict(CostoManoObra.objects.filter(periodo=periodo, obra_id__in=obras_ids).values_list('obra_id', 'monto'))
    values = calcular_item_costo(
        values,
        mos,
        no_prorrat,
        pro_manoobra
    )


    # subcontratos
    sub = dict(CostoSubContrato.objects.filter(periodo=periodo, obra_id__in=obras_ids).values_list('obra_id', 'monto'))
    values = calcular_item_costo(
        values,
        sub,
        no_prorrat
    )

    # gastos de equipos
    values = calcular_item_costo(
        values,
        totales,
        no_prorrat
    )

    # Materiales
    mat = dict(MaterialesTotal.objects.filter(periodo=periodo, obra__id__in=obras_ids).values_list('obra_id', 'monto'))
    values = calcular_item_costo(
        values,
        mat,
        no_prorrat,
        pro_materiales
    )
    # armamos la tabla de costos
    totales = [sum(i) for i in zip(*values)]
    total = sum(totales)
    values.append(totales)
    report = []
    report.append(headers)
    i = 0
    for x in tipo_costo_headers:
        l = list()
        l.append(x)
        l.extend(values[i])
        report.append(l)
        i += 1

    return report, total, dict(zip(no_prorrat, totales))


def get_ventas_costos(periodo, totales_costos):
    """Usando las claves del dict, buscar:
        Nombre de CC
        Certificaciones del periodo
        Subcontratos del periodo
        Calcular totales
        Calcular tota
    """
    ids = list(totales_costos.keys())
    obras = dict(Obras.objects.filter(id__in=ids).values_list('id', 'codigo'))
    cert = dict(Certificacion.objects.filter(periodo=periodo, obra_id__in=ids).values_list('obra_id', 'monto'))
    servicios = dict(ServicioPrestadoUN.objects.filter(periodo=periodo, obra_id__in=ids).values_list('obra_id', 'monto'))
    report = [['CC', ], ['Costos', ], ['Certificaciones', ], ['Servicios prestados a O/S', ], ['Diferencia', ], ]
    total = {'t_costos': 0, 't_certif': 0, 't_servicios': 0, 't_diff': 0}
    for x in ids:
        report[0].append(obras.get(x, 0))
        report[1].append(totales_costos.get(x, 0))
        total["t_costos"] += totales_costos.get(x, 0)
        report[2].append(cert.get(x, 0))
        total["t_certif"] += cert.get(x, 0)
        report[3].append(servicios.get(x, 0))
        total["t_servicios"] += servicios.get(x, 0)
        row_t = cert.get(x, 0) - totales_costos.get(x, 0) + servicios.get(x, 0)
        report[4].append(row_t)
        total["t_diff"] += row_t
    return report, total
