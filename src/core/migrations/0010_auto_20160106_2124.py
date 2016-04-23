# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_auto_20151228_2221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='obras',
            name='fecha_inicio',
            field=models.DateField(blank=True, db_column='FECHA_INICIO', null=True),
        ),
    ]
