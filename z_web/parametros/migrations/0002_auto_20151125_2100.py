# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parametros', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='familiaequipo',
            options={'verbose_name_plural': 'familias de equipo', 'verbose_name': 'familia de equipo'},
        ),
        migrations.AlterModelOptions(
            name='funcion',
            options={'verbose_name_plural': 'funciones', 'verbose_name': 'función'},
        ),
        migrations.AlterModelOptions(
            name='parametro',
            options={'verbose_name_plural': 'parametros', 'verbose_name': 'parametro'},
        ),
        migrations.AlterModelOptions(
            name='situacion',
            options={'verbose_name_plural': 'situaciones', 'verbose_name': 'situación'},
        ),
        migrations.AlterModelOptions(
            name='tipocosto',
            options={'verbose_name_plural': 'tipos de costo', 'verbose_name': 'tipo de costo'},
        ),
    ]
