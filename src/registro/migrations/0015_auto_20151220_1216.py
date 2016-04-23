# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0014_auto_20151220_1137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registroequipo',
            name='cant_combustible',
            field=models.CharField(null=True, blank=True, verbose_name='Litros combustible', db_column='CANT_COMBUSTIBLE', max_length=32),
        ),
        migrations.AlterField(
            model_name='registroequipo',
            name='datos_carga',
            field=models.IntegerField(verbose_name='¿Hay datos de cargas?', db_column='DATOS_CARGA'),
        ),
        migrations.AlterField(
            model_name='registroequipo',
            name='est_servicio',
            field=models.CharField(null=True, blank=True, verbose_name='Nombre plataforma', db_column='EST_SERVICIO', max_length=64),
        ),
        migrations.AlterField(
            model_name='registroequipo',
            name='estacion_servicio',
            field=models.ForeignKey(null=True, db_column='IDSERVICIO', to='core.EstServicio', blank=True, verbose_name='Plataforma de combustible'),
        ),
        migrations.AlterField(
            model_name='registroequipo',
            name='fin_horo',
            field=models.CharField(null=True, blank=True, verbose_name='Fin Horómetro', db_column='FIN_HORO', max_length=32),
        ),
        migrations.AlterField(
            model_name='registroequipo',
            name='fin_odo',
            field=models.CharField(null=True, blank=True, verbose_name='Fin Odómetro', db_column='FIN_ODO', max_length=32),
        ),
        migrations.AlterField(
            model_name='registroequipo',
            name='ini_horo',
            field=models.CharField(null=True, blank=True, verbose_name='Inicio Horómetro', db_column='INI_HORO', max_length=32),
        ),
        migrations.AlterField(
            model_name='registroequipo',
            name='ini_odo',
            field=models.CharField(null=True, blank=True, verbose_name='Inicio Odómetro', db_column='INI_ODO', max_length=32),
        ),
    ]
