# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parametros', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Equipos',
            fields=[
                ('id', models.AutoField(serialize=False, db_column='ID', primary_key=True)),
                ('n_interno', models.CharField(max_length=255, null=True, blank=True, db_column='N_INTERNO')),
                ('equipo', models.CharField(max_length=255, null=True, blank=True, db_column='EQUIPO')),
                ('marca', models.CharField(max_length=255, null=True, blank=True, db_column='MARCA')),
                ('modelo', models.CharField(max_length=255, null=True, blank=True, db_column='MODELO')),
                ('año', models.FloatField(null=True, blank=True, db_column='AÑO')),
                ('dominio', models.CharField(max_length=255, null=True, blank=True, db_column='DOMINIO')),
                ('vto_vtv', models.DateField(null=True, blank=True, db_column='VTO_VTV')),
                ('vto_seguro', models.DateField(null=True, blank=True, db_column='VTO_SEGURO')),
                ('descripcion_vto1', models.CharField(max_length=128, null=True, blank=True, db_column='DESCRIPCION_VTO1')),
                ('descripcion_vto2', models.CharField(max_length=128, null=True, blank=True, db_column='DESCRIPCION_VTO2')),
                ('descripcion_vto3', models.CharField(max_length=128, null=True, blank=True, db_column='DESCRIPCION_VTO3')),
                ('vto_otros1', models.DateField(null=True, blank=True, db_column='VTO_OTROS1')),
                ('vto_otros2', models.DateField(null=True, blank=True, db_column='VTO_OTROS2')),
                ('vto_otros3', models.DateField(null=True, blank=True, db_column='VTO_OTROS3')),
                ('familia_equipo', models.ForeignKey(null=True, to='parametros.FamiliaEquipo', blank=True, db_column='FAMILIA_EQUIPO_ID')),
            ],
            options={
                'db_table': 'equipos',
            },
        ),
        migrations.CreateModel(
            name='EstServicio',
            fields=[
                ('id', models.AutoField(serialize=False, db_column='ID', primary_key=True)),
                ('nombre', models.CharField(db_column='NOMBRE', max_length=128)),
            ],
            options={
                'db_table': 'est_servicio',
            },
        ),
        migrations.CreateModel(
            name='FrancoLicencia',
            fields=[
                ('id', models.AutoField(serialize=False, db_column='ID', primary_key=True)),
                ('ajuste_francos', models.IntegerField(db_column='AJUSTE_FRANCOS')),
                ('ajuste_licencias', models.IntegerField(db_column='AJUSTE_LICENCIAS')),
                ('pagados', models.IntegerField(db_column='PAGADOS')),
                ('solicitados1', models.IntegerField(null=True, blank=True, db_column='SOLICITADOS1')),
                ('solicitados2', models.IntegerField(null=True, blank=True, db_column='SOLICITADOS2')),
                ('entra1', models.DateField(null=True, blank=True, db_column='ENTRA1')),
                ('entra2', models.DateField(null=True, blank=True, db_column='ENTRA2')),
                ('sale1', models.DateField(null=True, blank=True, db_column='SALE1')),
                ('sale2', models.DateField(null=True, blank=True, db_column='SALE2')),
            ],
            options={
                'db_table': 'franco_licencia',
            },
        ),
        migrations.CreateModel(
            name='Obras',
            fields=[
                ('id', models.AutoField(serialize=False, db_column='ID', primary_key=True)),
                ('codigo', models.CharField(max_length=255, null=True, blank=True, db_column='CODIGO')),
                ('obra', models.CharField(max_length=255, null=True, blank=True, db_column='OBRA')),
                ('contrato', models.CharField(max_length=64, null=True, blank=True, db_column='CONTRATO')),
                ('comitente', models.CharField(max_length=255, null=True, blank=True, db_column='COMITENTE')),
                ('cuit', models.CharField(max_length=255, null=True, blank=True, db_column='CUIT')),
                ('lugar', models.CharField(max_length=255, null=True, blank=True, db_column='LUGAR')),
                ('plazo', models.CharField(max_length=255, null=True, blank=True, db_column='PLAZO')),
                ('fecha_inicio', models.CharField(max_length=255, null=True, blank=True, db_column='FECHA_INICIO')),
                ('responsable', models.CharField(max_length=255, null=True, blank=True, db_column='RESPONSABLE')),
                ('tiene_comida', models.TextField(db_column='TIENE_COMIDA')),
                ('tiene_vianda', models.TextField(db_column='TIENE_VIANDA')),
                ('tiene_desarraigo', models.TextField(db_column='TIENE_DESARRAIGO')),
                ('limite_vianda_doble', models.FloatField(db_column='LIMITE_VIANDA_DOBLE')),
                ('tiene_registro', models.TextField(db_column='TIENE_REGISTRO')),
                ('tiene_equipo', models.TextField(db_column='TIENE_EQUIPO')),
                ('descuenta_francos', models.TextField(db_column='DESCUENTA_FRANCOS')),
                ('descuenta_licencias', models.TextField(db_column='DESCUENTA_LICENCIAS')),
            ],
            options={
                'db_table': 'obras',
            },
        ),
        migrations.CreateModel(
            name='Operarios',
            fields=[
                ('id', models.AutoField(serialize=False, db_column='ID', primary_key=True)),
                ('n_legajo', models.CharField(max_length=255, null=True, blank=True, db_column='N_LEGAJO')),
                ('nombre', models.CharField(max_length=255, null=True, blank=True, db_column='NOMBRE')),
                ('cuil', models.CharField(max_length=255, null=True, blank=True, db_column='CUIL')),
                ('observaciones', models.CharField(max_length=255, null=True, blank=True, db_column='OBSERVACIONES')),
                ('funcion', models.IntegerField(db_column='FUNCION')),
                ('desarraigo', models.IntegerField(db_column='DESARRAIGO')),
                ('fecha_ingreso', models.DateField(null=True, blank=True, db_column='FECHA_INGRESO')),
                ('vto_carnet', models.DateField(null=True, blank=True, db_column='VTO_CARNET')),
                ('vto_psicofisico', models.DateField(null=True, blank=True, db_column='VTO_PSICOFISICO')),
                ('vto_cargagral', models.DateField(null=True, blank=True, db_column='VTO_CARGAGRAL')),
                ('vto_cargapeligrosa', models.DateField(null=True, blank=True, db_column='VTO_CARGAPELIGROSA')),
                ('descripcion_vto1', models.CharField(max_length=128, null=True, blank=True, db_column='DESCRIPCION_VTO1')),
                ('descripcion_vto2', models.CharField(max_length=128, null=True, blank=True, db_column='DESCRIPCION_VTO2')),
                ('descripcion_vto3', models.CharField(max_length=128, null=True, blank=True, db_column='DESCRIPCION_VTO3')),
                ('vto_otros1', models.DateField(null=True, blank=True, db_column='VTO_OTROS1')),
                ('vto_otros2', models.DateField(null=True, blank=True, db_column='VTO_OTROS2')),
                ('vto_otros3', models.DateField(null=True, blank=True, db_column='VTO_OTROS3')),
            ],
            options={
                'db_table': 'operarios',
            },
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(serialize=False, db_column='ID', primary_key=True)),
                ('user', models.CharField(db_column='USER', max_length=16)),
                ('pass_field', models.CharField(db_column='PASS', max_length=128)),
                ('rol', models.CharField(db_column='ROL', max_length=128)),
                ('fechabaja', models.DateTimeField(null=True, blank=True, db_column='FECHABAJA')),
            ],
            options={
                'db_table': 'usuario',
            },
        ),
        migrations.AddField(
            model_name='francolicencia',
            name='operario',
            field=models.ForeignKey(db_column='OPERARIO_ID', to='core.Operarios'),
        ),
    ]
