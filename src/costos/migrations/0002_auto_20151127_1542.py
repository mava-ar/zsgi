# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20151126_2055'),
        ('costos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='materialestotal',
            name='obra',
            field=models.ForeignKey(verbose_name='Centro de costo', related_name='costos_total_materiales', default=1, to='core.Obras'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='costoparametro',
            name='fecha_alta',
            field=models.DateField(verbose_name='Fecha de inicio de vigencia', auto_now_add=True, help_text='La fecha de inicio de vigencia se establecerá automaticamente al guardar.'),
        ),
        migrations.AlterField(
            model_name='costoparametro',
            name='fecha_baja',
            field=models.DateField(verbose_name='Fecha de fin de vigencia', null=True, default=None, help_text='La fecha de fin de vigencia, se establecerá automaticamente al añadir y/o modificar los valores de los parámetros de costos'),
        ),
        migrations.AlterField(
            model_name='materialestotal',
            name='periodo',
            field=models.ForeignKey(verbose_name='Periodo', related_name='costos_total_materiales', to='parametros.Periodo'),
        ),
    ]
