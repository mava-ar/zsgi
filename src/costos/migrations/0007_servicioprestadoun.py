# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20151126_2055'),
        ('parametros', '0004_auto_20151127_1904'),
        ('costos', '0006_costoposesion'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServicioPrestadoUN',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('monto', models.FloatField(verbose_name='$')),
                ('obra', models.ForeignKey(to='core.Obras', verbose_name='Centro de costo', related_name='costos_servicios_prestados')),
                ('periodo', models.ForeignKey(to='parametros.Periodo', verbose_name='Periodo', related_name='costos_servicios_prestados')),
            ],
            options={
                'verbose_name': 'costo de servicio prestado a UN',
                'verbose_name_plural': 'costos de servicios prestados a UN',
            },
        ),
    ]
