# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20151126_2045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='operarios',
            name='funcion',
            field=models.ForeignKey(db_column='FUNCION', to='parametros.Funcion'),
        ),
    ]
