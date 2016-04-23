# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('costos', '0013_auto_20151219_1104'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='costomanoobra',
            unique_together=set([('periodo', 'obra')]),
        ),
        migrations.AlterUniqueTogether(
            name='costoposesion',
            unique_together=set([('periodo', 'familia_equipo')]),
        ),
        migrations.AlterUniqueTogether(
            name='costosubcontrato',
            unique_together=set([('periodo', 'obra')]),
        ),
        migrations.AlterUniqueTogether(
            name='lubricantefluidoshidro',
            unique_together=set([('periodo', 'familia_equipo')]),
        ),
        migrations.AlterUniqueTogether(
            name='reservereparaciones',
            unique_together=set([('periodo', 'familia_equipo')]),
        ),
        migrations.AlterUniqueTogether(
            name='trenrodaje',
            unique_together=set([('periodo', 'familia_equipo')]),
        ),
    ]
