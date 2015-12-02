# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20151125_2230'),
    ]

    operations = [
        migrations.AlterField(
            model_name='obras',
            name='descuenta_francos',
            field=models.BooleanField(default=False, db_column='DESCUENTA_FRANCOS'),
        ),
        migrations.AlterField(
            model_name='obras',
            name='descuenta_licencias',
            field=models.BooleanField(default=False, db_column='DESCUENTA_LICENCIAS'),
        ),
        migrations.AlterField(
            model_name='obras',
            name='limite_vianda_doble',
            field=models.FloatField(default=2, db_column='LIMITE_VIANDA_DOBLE'),
        ),
        migrations.AlterField(
            model_name='obras',
            name='tiene_comida',
            field=models.BooleanField(default=True, db_column='TIENE_COMIDA'),
        ),
        migrations.AlterField(
            model_name='obras',
            name='tiene_desarraigo',
            field=models.BooleanField(default=True, db_column='TIENE_DESARRAIGO'),
        ),
        migrations.AlterField(
            model_name='obras',
            name='tiene_equipo',
            field=models.BooleanField(default=True, db_column='TIENE_EQUIPO'),
        ),
        migrations.AlterField(
            model_name='obras',
            name='tiene_registro',
            field=models.BooleanField(default=True, db_column='TIENE_REGISTRO'),
        ),
        migrations.AlterField(
            model_name='obras',
            name='tiene_vianda',
            field=models.BooleanField(default=True, db_column='TIENE_VIANDA'),
        ),
    ]
