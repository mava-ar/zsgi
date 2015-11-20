from django.db import models


class Alarma(models.Model):
    """
    Ok
    """
    alarmaid = models.AutoField(db_column='ALARMAID', primary_key=True)
    fecha = models.DateField(db_column='FECHA', blank=True, null=True)
    comentario = models.TextField(db_column='COMENTARIO', blank=True, null=True)
    fecha_previa = models.DateField(db_column='FECHA_PREVIA', blank=True, null=True)
    ri_id = models.ForeignKey('Ri', db_column='RI_ID', blank=True, null=True)
    nombre = models.CharField(db_column='NOMBRE', max_length=128, blank=True, null=True)

    class Meta:
        db_table = 'alarma'
        verbose_name = "alarma"
        verbose_name_plural = "alarmas"

    def __str__(self):
        return "{} ({})".format(self.nombre, self.fecha)


# class Combustible(models.Model):
    # combustibleid = models.AutoField(db_column='COMBUSTIBLEID', primary_key=True)
    # estacionid = models.IntegerField(db_column='ESTACIONID')  # Field name made lowercase.
    # fecha = models.DateField(db_column='FECHA')  # Field name made lowercase.
    # cantidad = models.FloatField(db_column='CANTIDAD')  # Field name made lowercase.
    # responsable = models.CharField(db_column='RESPONSABLE', max_length=128, blank=True, null=True)  # Field name made lowercase.

    # class Meta:
        # managed = False
        # db_table = 'combustible'

    # def __str__(self):
        # return "{}".format(self.estacionid)


# class Materiales(models.Model):
    # id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    # material = models.CharField(db_column='MATERIAL', max_length=255, blank=True, null=True)  # Field name made lowercase.
    # cantidad = models.CharField(db_column='CANTIDAD', max_length=255, blank=True, null=True)  # Field name made lowercase.
    # distancia = models.CharField(db_column='DISTANCIA', max_length=255, blank=True, null=True)  # Field name made lowercase.
    # viajes = models.CharField(db_column='VIAJES', max_length=255, blank=True, null=True)  # Field name made lowercase.
    # cantera_cargadero = models.CharField(db_column='CANTERA_CARGADERO', max_length=255, blank=True, null=True)  # Field name made lowercase.
    # id_registroequipo = models.IntegerField(db_column='ID_REGISTROEQUIPO')  # Field name made lowercase.

    # class Meta:
        # managed = False
        # db_table = 'materiales'


# class Partediario(models.Model):
    # id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    # situacion = models.IntegerField(db_column='SITUACION')  # Field name made lowercase.
    # numero = models.CharField(db_column='NUMERO', max_length=16, blank=True, null=True)  # Field name made lowercase.
    # operario = models.IntegerField(db_column='OPERARIO')  # Field name made lowercase.
    # funcion = models.IntegerField(db_column='FUNCION', blank=True, null=True)  # Field name made lowercase.
    # fecha = models.DateField(db_column='FECHA')  # Field name made lowercase.
    # obra = models.IntegerField(db_column='OBRA', blank=True, null=True)  # Field name made lowercase.
    # horario = models.IntegerField(db_column='HORARIO', blank=True, null=True)  # Field name made lowercase.
    # equipo = models.IntegerField(db_column='EQUIPO', blank=True, null=True)  # Field name made lowercase.
    # observaciones = models.TextField(db_column='OBSERVACIONES', blank=True, null=True)  # Field name made lowercase.
    # multifuncion = models.IntegerField(db_column='MULTIFUNCION', blank=True, null=True)  # Field name made lowercase.
    # desarraigo = models.IntegerField(db_column='DESARRAIGO', blank=True, null=True)  # Field name made lowercase.
    # comida = models.IntegerField(db_column='COMIDA', blank=True, null=True)  # Field name made lowercase.
    # vianda = models.IntegerField(db_column='VIANDA', blank=True, null=True)  # Field name made lowercase.
    # vianda_desa = models.IntegerField(db_column='VIANDA_DESA', blank=True, null=True)  # Field name made lowercase.

    # class Meta:
        # managed = False
        # db_table = 'partediario'


# class PrecioHistorico(models.Model):
    # fechaalta = models.DateField(db_column='fechaAlta', blank=True, null=True)  # Field name made lowercase.
    # fechabaja = models.DateField(db_column='fechaBaja', blank=True, null=True)  # Field name made lowercase.
    # valor = models.FloatField()
    # familia = models.ForeignKey(FamiliaEquipo, blank=True, null=True)
    # tipo = models.ForeignKey('TipoCosto', blank=True, null=True)

    # class Meta:
        # managed = False
        # db_table = 'precio_historico'


# class Registro(models.Model):
    # id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    # especial = models.IntegerField(db_column='ESPECIAL')  # Field name made lowercase.
    # dia = models.CharField(db_column='DIA', max_length=16)  # Field name made lowercase.
    # fecha = models.CharField(db_column='FECHA', max_length=16)  # Field name made lowercase.
    # hs_salida = models.TimeField(db_column='HS_SALIDA', blank=True, null=True)  # Field name made lowercase.
    # hs_llegada = models.TimeField(db_column='HS_LLEGADA', blank=True, null=True)  # Field name made lowercase.
    # hs_inicio = models.TimeField(db_column='HS_INICIO', blank=True, null=True)  # Field name made lowercase.
    # hs_fin = models.TimeField(db_column='HS_FIN', blank=True, null=True)  # Field name made lowercase.
    # hs_ialmuerzo = models.TimeField(db_column='HS_IALMUERZO', blank=True, null=True)  # Field name made lowercase.
    # hs_falmuerzo = models.TimeField(db_column='HS_FALMUERZO', blank=True, null=True)  # Field name made lowercase.
    # hs_normal = models.TimeField(db_column='HS_NORMAL', blank=True, null=True)  # Field name made lowercase.
    # hs_viaje = models.TimeField(db_column='HS_VIAJE', blank=True, null=True)  # Field name made lowercase.
    # hs_almuerzo = models.TimeField(db_column='HS_ALMUERZO', blank=True, null=True)  # Field name made lowercase.
    # hs_50 = models.TimeField(db_column='HS_50', blank=True, null=True)  # Field name made lowercase.
    # hs_100 = models.TimeField(db_column='HS_100', blank=True, null=True)  # Field name made lowercase.
    # hs_total = models.TimeField(db_column='HS_TOTAL', blank=True, null=True)  # Field name made lowercase.
    # hs_tarea = models.TimeField(db_column='HS_TAREA', blank=True, null=True)  # Field name made lowercase.

    # class Meta:
        # managed = False
        # db_table = 'registro'


# class RegistroEquipo(models.Model):
    # id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    # equipo = models.IntegerField(db_column='EQUIPO')  # Field name made lowercase.
    # ini_horo = models.CharField(db_column='INI_HORO', max_length=32, blank=True, null=True)  # Field name made lowercase.
    # fin_horo = models.CharField(db_column='FIN_HORO', max_length=32, blank=True, null=True)  # Field name made lowercase.
    # ini_odo = models.CharField(db_column='INI_ODO', max_length=32, blank=True, null=True)  # Field name made lowercase.
    # fin_odo = models.CharField(db_column='FIN_ODO', max_length=32, blank=True, null=True)  # Field name made lowercase.
    # cant_combustible = models.CharField(db_column='CANT_COMBUSTIBLE', max_length=32, blank=True, null=True)  # Field name made lowercase.
    # est_servicio = models.CharField(db_column='EST_SERVICIO', max_length=64, blank=True, null=True)  # Field name made lowercase.
    # tarea = models.TextField(db_column='TAREA', blank=True, null=True)  # Field name made lowercase.
    # datos_carga = models.IntegerField(db_column='DATOS_CARGA')  # Field name made lowercase.
    # idservicio = models.IntegerField(db_column='IDSERVICIO', blank=True, null=True)  # Field name made lowercase.

    # class Meta:
        # managed = False
        # db_table = 'registro_equipo'
