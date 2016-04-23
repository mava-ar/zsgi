# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='alarma',
            options={'verbose_name_plural': 'alarmas', 'verbose_name': 'alarma'},
        ),
        migrations.AlterModelOptions(
            name='combustible',
            options={'verbose_name_plural': 'entregas de combustible', 'verbose_name': 'entrega de combustible'},
        ),
        migrations.AlterModelOptions(
            name='materiales',
            options={'verbose_name_plural': 'materiales transportados', 'verbose_name': 'material transportado'},
        ),
        migrations.AlterModelOptions(
            name='partediario',
            options={'verbose_name_plural': 'partes diarios', 'verbose_name': 'parte diario'},
        ),
        migrations.AlterModelOptions(
            name='preciohistorico',
            options={'verbose_name_plural': 'precios históricos', 'verbose_name': 'precio histórico'},
        ),
        migrations.AlterModelOptions(
            name='registro',
            options={'verbose_name_plural': 'registros horario', 'verbose_name': 'registro horario'},
        ),
        migrations.AlterModelOptions(
            name='registroequipo',
            options={'verbose_name_plural': 'registros vehículares', 'verbose_name': 'registro vehícular'},
        ),
    ]
