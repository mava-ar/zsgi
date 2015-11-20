from __future__ import unicode_literals

from django.db import models

from parametros.models import FamiliaEquipo


class Equipos(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    n_interno = models.CharField(db_column='N_INTERNO', max_length=255, blank=True, null=True)  # Field name made lowercase.
    equipo = models.CharField(db_column='EQUIPO', max_length=255, blank=True, null=True)  # Field name made lowercase.
    marca = models.CharField(db_column='MARCA', max_length=255, blank=True, null=True)  # Field name made lowercase.
    modelo = models.CharField(db_column='MODELO', max_length=255, blank=True, null=True)  # Field name made lowercase.
    año = models.FloatField(db_column='AÑO', blank=True, null=True)  # Field name made lowercase.
    dominio = models.CharField(db_column='DOMINIO', max_length=255, blank=True, null=True)  # Field name made lowercase.
    vto_vtv = models.DateField(db_column='VTO_VTV', blank=True, null=True)  # Field name made lowercase.
    vto_seguro = models.DateField(db_column='VTO_SEGURO', blank=True, null=True)  # Field name made lowercase.
    descripcion_vto1 = models.CharField(db_column='DESCRIPCION_VTO1', max_length=128, blank=True, null=True)  # Field name made lowercase.
    descripcion_vto2 = models.CharField(db_column='DESCRIPCION_VTO2', max_length=128, blank=True, null=True)  # Field name made lowercase.
    descripcion_vto3 = models.CharField(db_column='DESCRIPCION_VTO3', max_length=128, blank=True, null=True)  # Field name made lowercase.
    vto_otros1 = models.DateField(db_column='VTO_OTROS1', blank=True, null=True)  # Field name made lowercase.
    vto_otros2 = models.DateField(db_column='VTO_OTROS2', blank=True, null=True)  # Field name made lowercase.
    vto_otros3 = models.DateField(db_column='VTO_OTROS3', blank=True, null=True)  # Field name made lowercase.
    familia_equipo = models.ForeignKey('FamiliaEquipo', db_column='FAMILIA_EQUIPO_ID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        verbose_name = "equipo"
        verbose_name_plural = "equipos"
        db_table = 'equipos'


class EstServicio(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)
    nombre = models.CharField(db_column='NOMBRE', max_length=128)

    class Meta:
        verbose_name = "estación de servicio"
        verbose_name_plural = "estaciones de servicio"
        db_table = 'est_servicio'


class FrancoLicencia(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)
    operario = models.ForeignKey('Operarios', db_column='OPERARIO_ID')
    ajuste_francos = models.IntegerField(db_column='AJUSTE_FRANCOS')
    ajuste_licencias = models.IntegerField(db_column='AJUSTE_LICENCIAS')
    pagados = models.IntegerField(db_column='PAGADOS')
    solicitados1 = models.IntegerField(db_column='SOLICITADOS1', blank=True, null=True)
    solicitados2 = models.IntegerField(db_column='SOLICITADOS2', blank=True, null=True)
    entra1 = models.DateField(db_column='ENTRA1', blank=True, null=True)
    entra2 = models.DateField(db_column='ENTRA2', blank=True, null=True)
    sale1 = models.DateField(db_column='SALE1', blank=True, null=True)
    sale2 = models.DateField(db_column='SALE2', blank=True, null=True)

    class Meta:
        verbose_name = "franco y licencia"
        verbose_name_plural = "francos y licencias"
        db_table = 'franco_licencia'


class Obras(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)
    codigo = models.CharField(db_column='CODIGO', max_length=255, blank=True, null=True)
    obra = models.CharField(db_column='OBRA', max_length=255, blank=True, null=True)
    contrato = models.CharField(db_column='CONTRATO', max_length=64, blank=True, null=True)
    comitente = models.CharField(db_column='COMITENTE', max_length=255, blank=True, null=True)
    cuit = models.CharField(db_column='CUIT', max_length=255, blank=True, null=True)
    lugar = models.CharField(db_column='LUGAR', max_length=255, blank=True, null=True)
    plazo = models.CharField(db_column='PLAZO', max_length=255, blank=True, null=True)
    fecha_inicio = models.CharField(db_column='FECHA_INICIO', max_length=255, blank=True, null=True)
    responsable = models.CharField(db_column='RESPONSABLE', max_length=255, blank=True, null=True)
    tiene_comida = models.TextField(db_column='TIENE_COMIDA')
    tiene_vianda = models.TextField(db_column='TIENE_VIANDA')
    tiene_desarraigo = models.TextField(db_column='TIENE_DESARRAIGO')
    limite_vianda_doble = models.FloatField(db_column='LIMITE_VIANDA_DOBLE')
    tiene_registro = models.TextField(db_column='TIENE_REGISTRO')
    tiene_equipo = models.TextField(db_column='TIENE_EQUIPO')
    descuenta_francos = models.TextField(db_column='DESCUENTA_FRANCOS')
    descuenta_licencias = models.TextField(db_column='DESCUENTA_LICENCIAS')

    class Meta:
        verbose_name = "obra"
        verbose_name_plural = "obras"
        db_table = 'obras'


class Operarios(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    n_legajo = models.CharField(db_column='N_LEGAJO', max_length=255, blank=True, null=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='NOMBRE', max_length=255, blank=True, null=True)  # Field name made lowercase.
    cuil = models.CharField(db_column='CUIL', max_length=255, blank=True, null=True)  # Field name made lowercase.
    observaciones = models.CharField(db_column='OBSERVACIONES', max_length=255, blank=True, null=True)  # Field name made lowercase.
    funcion = models.IntegerField(db_column='FUNCION')  # Field name made lowercase.
    desarraigo = models.IntegerField(db_column='DESARRAIGO')  # Field name made lowercase.
    fecha_ingreso = models.DateField(db_column='FECHA_INGRESO', blank=True, null=True)  # Field name made lowercase.
    vto_carnet = models.DateField(db_column='VTO_CARNET', blank=True, null=True)  # Field name made lowercase.
    vto_psicofisico = models.DateField(db_column='VTO_PSICOFISICO', blank=True, null=True)  # Field name made lowercase.
    vto_cargagral = models.DateField(db_column='VTO_CARGAGRAL', blank=True, null=True)  # Field name made lowercase.
    vto_cargapeligrosa = models.DateField(db_column='VTO_CARGAPELIGROSA', blank=True, null=True)  # Field name made lowercase.
    descripcion_vto1 = models.CharField(db_column='DESCRIPCION_VTO1', max_length=128, blank=True, null=True)  # Field name made lowercase.
    descripcion_vto2 = models.CharField(db_column='DESCRIPCION_VTO2', max_length=128, blank=True, null=True)  # Field name made lowercase.
    descripcion_vto3 = models.CharField(db_column='DESCRIPCION_VTO3', max_length=128, blank=True, null=True)  # Field name made lowercase.
    vto_otros1 = models.DateField(db_column='VTO_OTROS1', blank=True, null=True)  # Field name made lowercase.
    vto_otros2 = models.DateField(db_column='VTO_OTROS2', blank=True, null=True)  # Field name made lowercase.
    vto_otros3 = models.DateField(db_column='VTO_OTROS3', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        verbose_name = "operario"
        verbose_name_plural = "operarios"
        db_table = 'operarios'


class Usuario(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)
    user = models.CharField(db_column='USER', max_length=16)
    pass_field = models.CharField(db_column='PASS', max_length=128)
    rol = models.CharField(db_column='ROL', max_length=128)
    fechabaja = models.DateTimeField(db_column='FECHABAJA', blank=True, null=True)

    class Meta:
        verbose_name = "usuario"
        verbose_name_plural = "usuarios"
        db_table = 'usuario'
