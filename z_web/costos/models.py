from django.db import models
from django.db.models import Q
from core.models import Obras

from parametros.models import Periodo, FamiliaEquipo


class CostoManoObra(models.Model):
    """
    Costos de mano de obra por CC y periodo
    """
    obra = models.ForeignKey(Obras, verbose_name="Centro de Costo", related_name="costos_mo")
    periodo = models.ForeignKey(Periodo, verbose_name="Periodo", related_name="costos_mo")
    monto = models.FloatField(verbose_name="Monto ($)")

    class Meta:
        verbose_name_plural = "costos de mano de obra"
        verbose_name = "costo de mano de obra"

    def __str__(self):
        return "{} - {}".format(self.obra, self.periodo)


class CostoSubContrato(models.Model):
    """
    Costos por subcontratos
    """

    descripcion = models.CharField(verbose_name="Descripción", max_length=255, blank=True,
                                   help_text="Observaciones opcionales")
    obra = models.ForeignKey(Obras, verbose_name="Centro de costo", related_name="costos_subcontrato")
    periodo = models.ForeignKey(Periodo, verbose_name="Periodo", related_name="costos_subcontratos")
    monto = models.FloatField(verbose_name="Monto ($)")

    class Meta:
        verbose_name_plural = "costos por subcontrato"
        verbose_name = "costo de subcontrato"

    def __str__(self):
        return "{0} - {1}{2}".format(
            self.obra, self.periodo,
            "({})".format(self.descripcion) if self.descripcion else '')


class AbstractCosto(models.Model):
    """
    Clase genérica para costos comunes
    """
    familia_equipo = models.ForeignKey(FamiliaEquipo, verbose_name="Familia de equipo")
    periodo = models.ForeignKey(Periodo, verbose_name="Periodo")
    monto_hora = models.FloatField(verbose_name="$/hs")
    monto_mes = models.FloatField(verbose_name="$/mes")

    class Meta:
        abstract = True

    def __str__(self):
        return "{} de {} en {}".format(self._meta.verbose_name, self.familia_equipo, self.periodo)


class LubricanteFluidosHidro(AbstractCosto):

    class Meta:
        verbose_name = "costo de lubricantes y fluidos hidráulicos"
        verbose_name_plural = "costos de lubricantes y fluidos hidráulicos"


class TrenRodaje(AbstractCosto):

    class Meta:
        verbose_name = "costo de tren de rodaje"
        verbose_name_plural = "costos de tren de rodaje"


class ReserveReparaciones(AbstractCosto):

    class Meta:
        verbose_name = "costo de reserva de reparaciones"
        verbose_name_plural = "costos de reserva de reparaciones"


class CostoPosesion(AbstractCosto):
    monto_año = models.FloatField(verbose_name="$/año")

    class Meta:
        verbose_name = "costo de posesión"
        verbose_name_plural = "costos de posesión"


class MaterialesTotal(models.Model):
    """
    Total de costo de materiales por periodo
    """
    periodo = models.ForeignKey(Periodo, verbose_name="Periodo", related_name="costos_total_materiales")
    obra = models.ForeignKey(Obras, verbose_name="Centro de costo", related_name="costos_total_materiales")
    monto = models.FloatField(verbose_name="Costo ($)")

    class Meta:
        verbose_name = "costo total de materiales"
        verbose_name_plural = "costos totales de materiales"

    def __str__(self):
        return "{} - {}".format(self.obra, self.periodo)


class CostoParametroManager(models.Manager):
    def get_vigente_now(self):
        return super(CostoParametroManager, self).get_queryset().filter(fecha_baja__isnull=True).latest('fecha_alta')

    def get_vigente_el_dia(self, date):
        return super(CostoParametroManager, self).get_queryset().filter(
            Q(fecha_baja__gt=date) | Q(fecha_baja__isnull=True),
            fecha_alta__lte=date).latest('pk')

    def get_vigente_el_periodo(self, periodo):
        return super(CostoParametroManager, self).get_queryset().filter(
            Q(fecha_baja__gte=periodo.fecha_fin) | Q(fecha_baja__isnull=True),
            fecha_alta__lte=periodo.fecha_inicio)



class CostoParametro(models.Model):
    """
    Parámetros relacionados con los costos por periodo. Se mantiene trazabilidad
    al mantener las fechas de vigencia.
    """
    objects = models.Manager()
    vigentes = CostoParametroManager()

    horas_dia = models.PositiveSmallIntegerField(verbose_name="Hs/día", default=6)
    dias_mes = models.PositiveSmallIntegerField(verbose_name="Días/mes", default=20)
    horas_año = models.PositiveIntegerField(verbose_name="Hs/año", default=1440)
    pesos_usd = models.FloatField(verbose_name="$/USD", help_text="Valor del peso argentino frente al dolar.")
    fecha_alta = models.DateField(verbose_name="Fecha de inicio de vigencia", auto_now_add=True,
                                  help_text="La fecha de inicio de vigencia se establecerá automaticamente al guardar.")
    fecha_baja = models.DateField(verbose_name="Fecha de fin de vigencia", null=True, default=None,
                                  help_text="La fecha de fin de vigencia, se establecerá automaticamente al añadir y/o "
                                            "modificar los valores de los parámetros de costos")

    def __str__(self):
        if self.fecha_baja:
            return "{} - {}".format(self.fecha_alta, self.fecha_baja)
        else:
            return "Vigente desde {}".format(self.fecha_alta)

    class Meta:
        verbose_name = "parametro de costo"
        verbose_name_plural = "parametros de costos"


class ServicioPrestadoUN(models.Model):
    """
    Servicios prestados a otras Unidades de Negocio
    """
    periodo = models.ForeignKey(Periodo, verbose_name="Periodo", related_name="costos_servicios_prestados")
    obra = models.ForeignKey(Obras, verbose_name="Centro de costo", related_name="costos_servicios_prestados")
    monto = models.FloatField(verbose_name="Costo ($)")

    class Meta:
        verbose_name = "costo de servicio prestado a UN"
        verbose_name_plural = "costos de servicios prestados a UN"

    def __str__(self):
        return "{} - {}".format(self.obra, self.periodo)
