# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parametros', '0003_periodo'),
        ('core', '0006_auto_20151126_2055'),
    ]

    operations = [
        migrations.CreateModel(
            name='CostoManoObra',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('monto', models.FloatField(verbose_name='Monto ($)')),
                ('obra', models.ForeignKey(related_name='costos_mo', to='core.Obras', verbose_name='Centro de Costo')),
                ('periodo', models.ForeignKey(related_name='costos_mo', to='parametros.Periodo', verbose_name='Periodo')),
            ],
            options={
                'verbose_name': 'costo de mano de obra',
                'verbose_name_plural': 'costos de mono de obra',
            },
        ),
        migrations.CreateModel(
            name='CostoParametro',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('horas_dia', models.PositiveSmallIntegerField(verbose_name='Hs/día', default=6)),
                ('dias_mes', models.PositiveSmallIntegerField(verbose_name='Días/mes', default=20)),
                ('horas_año', models.PositiveIntegerField(verbose_name='Hs/año', default=1440)),
                ('pesos_usd', models.FloatField(help_text='Valor del peso argentino frente al dolar.', verbose_name='$/USD')),
                ('fecha_alta', models.DateField(verbose_name='Fecha de inicio de vigencia', auto_now_add=True)),
                ('fecha_baja', models.DateField(verbose_name='Fecha de fin de vigencia', default=None, null=True)),
            ],
            options={
                'verbose_name': 'parametro de costo',
                'verbose_name_plural': 'parametros de costos',
            },
        ),
        migrations.CreateModel(
            name='CostoSubContrato',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('descripcion', models.CharField(verbose_name='Descripción', max_length=255)),
                ('tipo', models.CharField(verbose_name='Tipo de subcontrato', default='a', max_length=1, choices=[('a', 'NORMAL')])),
                ('monto', models.FloatField(verbose_name='Monto ($)')),
                ('obra', models.ForeignKey(related_name='costos_subcontrato', to='core.Obras', verbose_name='Centro de costo')),
                ('periodo', models.ForeignKey(related_name='costos_subcontratos', to='parametros.Periodo', verbose_name='Periodo')),
            ],
            options={
                'verbose_name': 'costo de subcontrato',
                'verbose_name_plural': 'costos por subcontrato',
            },
        ),
        migrations.CreateModel(
            name='LubricanteFluidosHidro',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('monto_hora', models.FloatField(verbose_name='$/hs')),
                ('monto_mes', models.FloatField(verbose_name='$/mes')),
                ('familia_equipo', models.ForeignKey(to='parametros.FamiliaEquipo', verbose_name='Familia de equipo')),
                ('periodo', models.ForeignKey(to='parametros.Periodo', verbose_name='Periodo')),
            ],
            options={
                'verbose_name': 'costo de lubricantes y fluidos hidráulicos',
                'verbose_name_plural': 'costos de lubricantes y fluidos hidráulicos',
            },
        ),
        migrations.CreateModel(
            name='MaterialesTotal',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('monto', models.FloatField(verbose_name='$')),
                ('periodo', models.ForeignKey(related_name='costos_total_materiles', to='parametros.Periodo', verbose_name='Periodo')),
            ],
            options={
                'verbose_name': 'costo total de materiales',
                'verbose_name_plural': 'costos totales de materiales',
            },
        ),
        migrations.CreateModel(
            name='ReserveReparaciones',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('monto_hora', models.FloatField(verbose_name='$/hs')),
                ('monto_mes', models.FloatField(verbose_name='$/mes')),
                ('familia_equipo', models.ForeignKey(to='parametros.FamiliaEquipo', verbose_name='Familia de equipo')),
                ('periodo', models.ForeignKey(to='parametros.Periodo', verbose_name='Periodo')),
            ],
            options={
                'verbose_name': 'costo de reserva de reparaciones',
                'verbose_name_plural': 'costos de reserva de reparaciones',
            },
        ),
        migrations.CreateModel(
            name='TrenRodaje',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('monto_hora', models.FloatField(verbose_name='$/hs')),
                ('monto_mes', models.FloatField(verbose_name='$/mes')),
                ('familia_equipo', models.ForeignKey(to='parametros.FamiliaEquipo', verbose_name='Familia de equipo')),
                ('periodo', models.ForeignKey(to='parametros.Periodo', verbose_name='Periodo')),
            ],
            options={
                'verbose_name': 'costo de tren de rodaje',
                'verbose_name_plural': 'costos de tren de rodaje',
            },
        ),
    ]
