# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0005_auto_20151125_2133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='materiales',
            name='cantidad',
            field=models.CharField(max_length=64, null=True, blank=True, db_column='CANTIDAD'),
        ),
        migrations.AlterField(
            model_name='materiales',
            name='distancia',
            field=models.CharField(max_length=64, blank=True, db_column='DISTANCIA', null=True),
        ),
        migrations.AlterField(
            model_name='materiales',
            name='id_registroequipo',
            field=models.ForeignKey(to='registro.RegistroEquipo', db_column='ID_REGISTROEQUIPO'),
        ),
        migrations.AlterField(
            model_name='materiales',
            name='material',
            field=models.CharField(blank=True, db_column='MATERIAL', max_length=255, null=True, choices=[('agua', 'Agua'), ('arcilla', 'Arcilla'), ('arena', 'Arena'), ('calcareo', 'Calcareo'), ('destape', 'Destape'), ('otro', 'Otro'), ('relleno', 'Relleno'), ('yeso', 'Yeso')]),
        ),
        migrations.AlterField(
            model_name='materiales',
            name='viajes',
            field=models.PositiveSmallIntegerField(blank=True, db_column='VIAJES', null=True),
        ),
    ]
