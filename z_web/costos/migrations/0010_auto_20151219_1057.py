# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parametros', '0004_auto_20151127_1904'),
        ('costos', '0009_costoparametro_precio_go'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='costoparametro',
            name='fecha_alta',
        ),
        migrations.RemoveField(
            model_name='costoparametro',
            name='fecha_baja',
        ),
        migrations.AddField(
            model_name='costoparametro',
            name='periodo',
            field=models.ForeignKey(verbose_name='Periodo', to='parametros.Periodo', default=1, related_name='parametros_costos'),
            preserve_default=False,
        ),
    ]
