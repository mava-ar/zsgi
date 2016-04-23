# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parametros', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Alarma',
            fields=[
                ('alarmaid', models.AutoField(serialize=False, db_column='ALARMAID', primary_key=True)),
                ('fecha', models.DateField(blank=True, db_column='FECHA', null=True)),
                ('comentario', models.TextField(blank=True, db_column='COMENTARIO', null=True)),
                ('fecha_previa', models.DateField(blank=True, db_column='FECHA_PREVIA', null=True)),
                ('ri_id', models.IntegerField(blank=True, db_column='RI_ID', null=True)),
                ('nombre', models.CharField(blank=True, max_length=128, db_column='NOMBRE', null=True)),
            ],
            options={
                'db_table': 'alarma',
            },
        ),
        migrations.CreateModel(
            name='Combustible',
            fields=[
                ('combustibleid', models.AutoField(serialize=False, db_column='COMBUSTIBLEID', primary_key=True)),
                ('estacionid', models.IntegerField(db_column='ESTACIONID')),
                ('fecha', models.DateField(db_column='FECHA')),
                ('cantidad', models.FloatField(db_column='CANTIDAD')),
                ('responsable', models.CharField(blank=True, max_length=128, db_column='RESPONSABLE', null=True)),
            ],
            options={
                'db_table': 'combustible',
            },
        ),
        migrations.CreateModel(
            name='Materiales',
            fields=[
                ('id', models.AutoField(serialize=False, db_column='ID', primary_key=True)),
                ('material', models.CharField(blank=True, max_length=255, db_column='MATERIAL', null=True)),
                ('cantidad', models.CharField(blank=True, max_length=255, db_column='CANTIDAD', null=True)),
                ('distancia', models.CharField(blank=True, max_length=255, db_column='DISTANCIA', null=True)),
                ('viajes', models.CharField(blank=True, max_length=255, db_column='VIAJES', null=True)),
                ('cantera_cargadero', models.CharField(blank=True, max_length=255, db_column='CANTERA_CARGADERO', null=True)),
                ('id_registroequipo', models.IntegerField(db_column='ID_REGISTROEQUIPO')),
            ],
            options={
                'db_table': 'materiales',
            },
        ),
        migrations.CreateModel(
            name='Partediario',
            fields=[
                ('id', models.AutoField(serialize=False, db_column='ID', primary_key=True)),
                ('situacion', models.IntegerField(db_column='SITUACION')),
                ('numero', models.CharField(blank=True, max_length=16, db_column='NUMERO', null=True)),
                ('operario', models.IntegerField(db_column='OPERARIO')),
                ('funcion', models.IntegerField(blank=True, db_column='FUNCION', null=True)),
                ('fecha', models.DateField(db_column='FECHA')),
                ('obra', models.IntegerField(blank=True, db_column='OBRA', null=True)),
                ('horario', models.IntegerField(blank=True, db_column='HORARIO', null=True)),
                ('equipo', models.IntegerField(blank=True, db_column='EQUIPO', null=True)),
                ('observaciones', models.TextField(blank=True, db_column='OBSERVACIONES', null=True)),
                ('multifuncion', models.IntegerField(blank=True, db_column='MULTIFUNCION', null=True)),
                ('desarraigo', models.IntegerField(blank=True, db_column='DESARRAIGO', null=True)),
                ('comida', models.IntegerField(blank=True, db_column='COMIDA', null=True)),
                ('vianda', models.IntegerField(blank=True, db_column='VIANDA', null=True)),
                ('vianda_desa', models.IntegerField(blank=True, db_column='VIANDA_DESA', null=True)),
            ],
            options={
                'db_table': 'partediario',
            },
        ),
        migrations.CreateModel(
            name='PrecioHistorico',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('fechaalta', models.DateField(blank=True, db_column='fechaAlta', null=True)),
                ('fechabaja', models.DateField(blank=True, db_column='fechaBaja', null=True)),
                ('valor', models.FloatField()),
                ('familia', models.ForeignKey(to='parametros.FamiliaEquipo', blank=True, null=True)),
                ('tipo', models.ForeignKey(to='parametros.TipoCosto', blank=True, null=True)),
            ],
            options={
                'db_table': 'precio_historico',
            },
        ),
        migrations.CreateModel(
            name='Registro',
            fields=[
                ('id', models.AutoField(serialize=False, db_column='ID', primary_key=True)),
                ('especial', models.IntegerField(db_column='ESPECIAL')),
                ('dia', models.CharField(max_length=16, db_column='DIA')),
                ('fecha', models.CharField(max_length=16, db_column='FECHA')),
                ('hs_salida', models.TimeField(blank=True, db_column='HS_SALIDA', null=True)),
                ('hs_llegada', models.TimeField(blank=True, db_column='HS_LLEGADA', null=True)),
                ('hs_inicio', models.TimeField(blank=True, db_column='HS_INICIO', null=True)),
                ('hs_fin', models.TimeField(blank=True, db_column='HS_FIN', null=True)),
                ('hs_ialmuerzo', models.TimeField(blank=True, db_column='HS_IALMUERZO', null=True)),
                ('hs_falmuerzo', models.TimeField(blank=True, db_column='HS_FALMUERZO', null=True)),
                ('hs_normal', models.TimeField(blank=True, db_column='HS_NORMAL', null=True)),
                ('hs_viaje', models.TimeField(blank=True, db_column='HS_VIAJE', null=True)),
                ('hs_almuerzo', models.TimeField(blank=True, db_column='HS_ALMUERZO', null=True)),
                ('hs_50', models.TimeField(blank=True, db_column='HS_50', null=True)),
                ('hs_100', models.TimeField(blank=True, db_column='HS_100', null=True)),
                ('hs_total', models.TimeField(blank=True, db_column='HS_TOTAL', null=True)),
                ('hs_tarea', models.TimeField(blank=True, db_column='HS_TAREA', null=True)),
            ],
            options={
                'db_table': 'registro',
            },
        ),
        migrations.CreateModel(
            name='RegistroEquipo',
            fields=[
                ('id', models.AutoField(serialize=False, db_column='ID', primary_key=True)),
                ('equipo', models.IntegerField(db_column='EQUIPO')),
                ('ini_horo', models.CharField(blank=True, max_length=32, db_column='INI_HORO', null=True)),
                ('fin_horo', models.CharField(blank=True, max_length=32, db_column='FIN_HORO', null=True)),
                ('ini_odo', models.CharField(blank=True, max_length=32, db_column='INI_ODO', null=True)),
                ('fin_odo', models.CharField(blank=True, max_length=32, db_column='FIN_ODO', null=True)),
                ('cant_combustible', models.CharField(blank=True, max_length=32, db_column='CANT_COMBUSTIBLE', null=True)),
                ('est_servicio', models.CharField(blank=True, max_length=64, db_column='EST_SERVICIO', null=True)),
                ('tarea', models.TextField(blank=True, db_column='TAREA', null=True)),
                ('datos_carga', models.IntegerField(db_column='DATOS_CARGA')),
                ('idservicio', models.IntegerField(blank=True, db_column='IDSERVICIO', null=True)),
            ],
            options={
                'db_table': 'registro_equipo',
            },
        ),
    ]
