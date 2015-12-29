# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('costos', '0014_auto_20151219_1105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicioprestadoun',
            name='obra',
            field=models.ForeignKey(verbose_name='Centro de costo', to='core.Obras', related_name='costos_servicios_xobra'),
        ),
        migrations.AlterField(
            model_name='servicioprestadoun',
            name='periodo',
            field=models.ForeignKey(verbose_name='Periodo', to='parametros.Periodo', related_name='costos_servicios_xperiodo'),
        ),
    ]
