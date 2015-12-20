# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0015_auto_20151220_1216'),
    ]

    operations = [
        migrations.AddField(
            model_name='registroequipo',
            name='cantera_cargadero',
            field=models.CharField(null=True, blank=True, verbose_name='Cantera/Cargadero', max_length=255),
        ),
        migrations.AddField(
            model_name='registroequipo',
            name='cantidad',
            field=models.FloatField(null=True, verbose_name='Cantidad', blank=True),
        ),
        migrations.AddField(
            model_name='registroequipo',
            name='distancia',
            field=models.FloatField(null=True, verbose_name='Distancia', blank=True),
        ),
        migrations.AddField(
            model_name='registroequipo',
            name='material',
            field=models.CharField(null=True, blank=True, choices=[('agua', 'Agua'), ('arcilla', 'Arcilla'), ('arena', 'Arena'), ('calcareo', 'Calcareo'), ('destape', 'Destape'), ('otro', 'Otro'), ('relleno', 'Relleno'), ('yeso', 'Yeso')], verbose_name='Material Transportado', max_length=255),
        ),
        migrations.AddField(
            model_name='registroequipo',
            name='viajes',
            field=models.PositiveSmallIntegerField(null=True, verbose_name='Cantidad de viajes', blank=True),
        ),
    ]
