# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parametros', '0002_auto_20151125_2100'),
    ]

    operations = [
        migrations.CreateModel(
            name='Periodo',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('descripcion', models.CharField(max_length=255, verbose_name='Periodo')),
                ('fecha_inicio', models.DateField(verbose_name='Fecha de inicio')),
                ('fecha_fin', models.DateField(verbose_name='Fecha de cierre')),
            ],
            options={
                'verbose_name_plural': 'periodos',
                'verbose_name': 'periodo',
            },
        ),
    ]
