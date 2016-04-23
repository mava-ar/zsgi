# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('costos', '0007_servicioprestadoun'),
    ]

    operations = [
        migrations.AlterField(
            model_name='materialestotal',
            name='monto',
            field=models.FloatField(verbose_name='Costo ($)'),
        ),
        migrations.AlterField(
            model_name='servicioprestadoun',
            name='monto',
            field=models.FloatField(verbose_name='Costo ($)'),
        ),
    ]
