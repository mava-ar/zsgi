# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='InformesHoras',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('id_operario', models.IntegerField(db_column='ID_OPERARIO')),
                ('multi_fc', models.IntegerField(db_column='MULTI_FC')),
                ('total_hs_viaje', models.FloatField(db_column='TOTAL_HS_VIAJE')),
                ('total_50', models.FloatField(db_column='TOTAL_50')),
                ('total_100', models.FloatField(db_column='TOTAL_100')),
                ('total_normal', models.FloatField(db_column='TOTAL_NORMAL')),
                ('total_tarea', models.FloatField(db_column='TOTAL_TAREA')),
                ('periodo', models.CharField(max_length=32, db_column='PERIODO')),
                ('desde_f', models.DateField(db_column='DESDE_F')),
                ('hasta_f', models.DateField(db_column='HASTA_F')),
                ('x100obra', models.CharField(max_length=128, db_column='X100OBRA', null=True, blank=True)),
            ],
            options={
                'db_table': 'informes_horas',
            },
        ),
        migrations.CreateModel(
            name='OrdenTrabajo',
            fields=[
                ('ordentrabajoid', models.AutoField(db_column='OrdenTrabajoID', primary_key=True, serialize=False)),
                ('fecha', models.DateField(db_column='Fecha', blank=True, null=True)),
                ('km', models.CharField(max_length=128, db_column='Km', null=True, blank=True)),
                ('detalleservicio', models.TextField(db_column='DetalleServicio', blank=True, null=True)),
                ('ninternoid', models.IntegerField(db_column='NInternoID')),
                ('manodeobra', models.CharField(max_length=128, db_column='ManoDeObra', null=True, blank=True)),
                ('aperturafecha', models.DateField(db_column='AperturaFecha', blank=True, null=True)),
                ('cierrefecha', models.DateField(db_column='CierreFecha', blank=True, null=True)),
                ('mantenimiento', models.CharField(max_length=64, db_column='Mantenimiento')),
                ('ninterno', models.CharField(max_length=128, db_column='NInterno', null=True, blank=True)),
                ('hs', models.CharField(max_length=128, db_column='Hs', null=True, blank=True)),
                ('solicitante', models.CharField(max_length=128, db_column='Solicitante', null=True, blank=True)),
                ('importe', models.CharField(max_length=45, db_column='Importe', null=True, blank=True)),
            ],
            options={
                'db_table': 'orden_trabajo',
            },
        ),
        migrations.CreateModel(
            name='Ri',
            fields=[
                ('riid', models.AutoField(db_column='RIID', primary_key=True, serialize=False)),
                ('ri_num', models.CharField(max_length=45, db_column='RI_NUM', null=True, blank=True)),
                ('obraid', models.IntegerField(db_column='OBRAID', blank=True, null=True)),
                ('observaciones', models.TextField(db_column='OBSERVACIONES', blank=True, null=True)),
                ('solicitante', models.CharField(max_length=128, db_column='SOLICITANTE', null=True, blank=True)),
                ('fecha_creacion', models.CharField(max_length=45, db_column='FECHA_CREACION', null=True, blank=True)),
            ],
            options={
                'db_table': 'ri',
            },
        ),
        migrations.CreateModel(
            name='RiItem',
            fields=[
                ('riitemid', models.AutoField(db_column='riItemId', primary_key=True, serialize=False)),
                ('riid', models.IntegerField(db_column='riId', blank=True, null=True)),
                ('cantidad', models.CharField(max_length=45, blank=True, null=True)),
                ('unidad', models.CharField(max_length=45, blank=True, null=True)),
                ('detalle', models.TextField(blank=True, null=True)),
                ('observacion', models.TextField(blank=True, null=True)),
                ('oc_num', models.CharField(max_length=45, blank=True, null=True)),
                ('proveedor', models.CharField(max_length=128, blank=True, null=True)),
                ('fecha_entrega', models.DateField(blank=True, null=True)),
                ('fecha_oc', models.DateField(blank=True, null=True)),
                ('fecha_emision', models.DateField(blank=True, null=True)),
                ('fecha_necesidad', models.DateField(blank=True, null=True)),
                ('valor', models.CharField(max_length=128)),
            ],
            options={
                'db_table': 'ri_item',
            },
        ),
    ]
