from django.db import models


class Ri(models.Model):
    """
    ok
    """
    riid = models.AutoField(db_column='RIID', primary_key=True)
    ri_num = models.CharField(db_column='RI_NUM', max_length=45, blank=True, null=True)
    obraid = models.ForeignKey('Obras', db_column='OBRAID', blank=True, null=True, related_name="ris")
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
    cantidad = models.PositiveIntegerField(blank=True, null=True, default=1)
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


# class InformesHoras(models.Model):
    # id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    # id_operario = models.IntegerField(db_column='ID_OPERARIO')  # Field name made lowercase.
    # multi_fc = models.IntegerField(db_column='MULTI_FC')  # Field name made lowercase.
    # total_hs_viaje = models.FloatField(db_column='TOTAL_HS_VIAJE')  # Field name made lowercase.
    # total_50 = models.FloatField(db_column='TOTAL_50')  # Field name made lowercase.
    # total_100 = models.FloatField(db_column='TOTAL_100')  # Field name made lowercase.
    # total_normal = models.FloatField(db_column='TOTAL_NORMAL')  # Field name made lowercase.
    # total_tarea = models.FloatField(db_column='TOTAL_TAREA')  # Field name made lowercase.
    # periodo = models.CharField(db_column='PERIODO', max_length=32)  # Field name made lowercase.
    # desde_f = models.DateField(db_column='DESDE_F')  # Field name made lowercase.
    # hasta_f = models.DateField(db_column='HASTA_F')  # Field name made lowercase.
    # x100obra = models.CharField(db_column='X100OBRA', max_length=128, blank=True, null=True)  # Field name made lowercase.

    # class Meta:
        # managed = False
        # db_table = 'informes_horas'


# class OrdenTrabajo(models.Model):
    # ordentrabajoid = models.AutoField(db_column='OrdenTrabajoID', primary_key=True)  # Field name made lowercase.
    # fecha = models.DateField(db_column='Fecha', blank=True, null=True)  # Field name made lowercase.
    # km = models.CharField(db_column='Km', max_length=128, blank=True, null=True)  # Field name made lowercase.
    # detalleservicio = models.TextField(db_column='DetalleServicio', blank=True, null=True)  # Field name made lowercase.
    # ninternoid = models.IntegerField(db_column='NInternoID')  # Field name made lowercase.
    # manodeobra = models.CharField(db_column='ManoDeObra', max_length=128, blank=True, null=True)  # Field name made lowercase.
    # aperturafecha = models.DateField(db_column='AperturaFecha', blank=True, null=True)  # Field name made lowercase.
    # cierrefecha = models.DateField(db_column='CierreFecha', blank=True, null=True)  # Field name made lowercase.
    # mantenimiento = models.CharField(db_column='Mantenimiento', max_length=64)  # Field name made lowercase.
    # ninterno = models.CharField(db_column='NInterno', max_length=128, blank=True, null=True)  # Field name made lowercase.
    # hs = models.CharField(db_column='Hs', max_length=128, blank=True, null=True)  # Field name made lowercase.
    # solicitante = models.CharField(db_column='Solicitante', max_length=128, blank=True, null=True)  # Field name made lowercase.
    # importe = models.CharField(db_column='Importe', max_length=45, blank=True, null=True)  # Field name made lowercase.

    # class Meta:
        # managed = False
        # db_table = 'orden_trabajo'
