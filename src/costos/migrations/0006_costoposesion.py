# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parametros', '0004_auto_20151127_1904'),
        ('costos', '0005_remove_costosubcontrato_tipo'),
    ]

    operations = [
        migrations.CreateModel(
            name='CostoPosesion',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('monto_hora', models.FloatField(verbose_name='$/hs')),
                ('monto_mes', models.FloatField(verbose_name='$/mes')),
                ('monto_año', models.FloatField(verbose_name='$/año')),
                ('familia_equipo', models.ForeignKey(verbose_name='Familia de equipo', to='parametros.FamiliaEquipo')),
                ('periodo', models.ForeignKey(verbose_name='Periodo', to='parametros.Periodo')),
            ],
            options={
                'verbose_name_plural': 'costos de posesión',
                'verbose_name': 'costo de posesión',
            },
        ),
    ]
