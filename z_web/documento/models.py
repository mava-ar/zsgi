from django.db import models

from core.models import Obras, Operarios


class Ri(models.Model):
    """
    ok
    """
    riid = models.AutoField(db_column='RIID', primary_key=True)
    ri_num = models.CharField(db_column='RI_NUM', max_length=45, blank=True, null=True)
    obraid = models.ForeignKey(Obras, db_column='OBRAID', blank=True, null=True, related_name="ris")
    observaciones = models.TextField(db_column='OBSERVACIONES', blank=True, null=True)
    solicitante = models.CharField(db_column='SOLICITANTE', max_length=128, blank=True, null=True)
    fecha_creacion = models.DateField(db_column='FECHA_CREACION', blank=True, null=True)

    class Meta:
        db_table = 'ri'
        verbose_name = "requerimiento interno"
        verbose_name_plural = "requerimientos internos"

    def __str__(self):
        return "({}) {} - {})".format(
            self.ri_num, self.solicitante,
            " - %s" % self.observaciones if self.observaciones else '')


class RiItem(models.Model):
    """
    OK
    """
    riitemid = models.AutoField(db_column='riItemId', primary_key=True)
    riid = models.ForeignKey(Ri, db_column='riId', related_name="items", null=True)
    cantidad = models.CharField(max_length=255, blank=True, null=True)
    unidad = models.CharField(max_length=45, blank=True, null=True)
    detalle = models.TextField(blank=True, null=True)
    observacion = models.TextField(blank=True, null=True)
    oc_num = models.CharField(max_length=45, blank=True, null=True)
    proveedor = models.CharField(max_length=128, blank=True, null=True)
    fecha_entrega = models.DateField(blank=True, null=True)
    fecha_oc = models.DateField(blank=True, null=True)
    fecha_emision = models.DateField(blank=True, null=True)
    fecha_necesidad = models.DateField(blank=True, null=True)
    valor = models.CharField(max_length=128)

    class Meta:
        db_table = 'ri_item'
        verbose_name = "item de requerimiento interno"
        verbose_name_plural = "itemes de requerimiento interno"

    def __str__(self):
        return "{} {} - {} {}".format(self.cantidad, self.unidad,
                                      self.detalle, self.proveedor)


class InformesHoras(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)
    operario = models.ForeignKey(Operarios, db_column='ID_OPERARIO')
    multi_fc = models.IntegerField(db_column='MULTI_FC')
    total_hs_viaje = models.FloatField(db_column='TOTAL_HS_VIAJE')
    total_50 = models.FloatField(db_column='TOTAL_50')
    total_100 = models.FloatField(db_column='TOTAL_100')
    total_normal = models.FloatField(db_column='TOTAL_NORMAL')
    total_tarea = models.FloatField(db_column='TOTAL_TAREA')
    periodo = models.CharField(db_column='PERIODO', max_length=32)
    desde_f = models.DateField(db_column='DESDE_F')
    hasta_f = models.DateField(db_column='HASTA_F')
    x100obra = models.CharField(db_column='X100OBRA', max_length=128, blank=True, null=True)

    class Meta:
        db_table = 'informes_horas'
        verbose_name = "informe de registro horario"
        verbose_name_plural = "informes de registro horario"


class OrdenTrabajo(models.Model):
    ordentrabajoid = models.AutoField(db_column='OrdenTrabajoID', primary_key=True)
    fecha = models.DateField(db_column='Fecha', blank=True, null=True)
    km = models.CharField(db_column='Km', max_length=128, blank=True, null=True)
    detalleservicio = models.TextField(db_column='DetalleServicio', blank=True, null=True)
    ninternoid = models.IntegerField(db_column='NInternoID')
    manodeobra = models.CharField(db_column='ManoDeObra', max_length=128, blank=True, null=True)
    aperturafecha = models.DateField(db_column='AperturaFecha', blank=True, null=True)
    cierrefecha = models.DateField(db_column='CierreFecha', blank=True, null=True)
    mantenimiento = models.CharField(db_column='Mantenimiento', max_length=64)
    ninterno = models.CharField(db_column='NInterno', max_length=128, blank=True, null=True)
    hs = models.CharField(db_column='Hs', max_length=128, blank=True, null=True)
    solicitante = models.CharField(db_column='Solicitante', max_length=128, blank=True, null=True)
    importe = models.CharField(db_column='Importe', max_length=45, blank=True, null=True)

    class Meta:
        db_table = 'orden_trabajo'
        verbose_name = "orden de trabajo"
        verbose_name_plural = "órdenes de trabajo"
