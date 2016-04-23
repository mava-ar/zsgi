# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('costos', '0010_auto_20151219_1057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='costoparametro',
            name='periodo',
            field=models.OneToOneField(verbose_name='Periodo', related_name='parametros_costos', to='parametros.Periodo'),
        ),
    ]
