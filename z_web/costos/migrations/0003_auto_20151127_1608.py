# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('costos', '0002_auto_20151127_1542'),
    ]

    operations = [
        migrations.AlterField(
            model_name='costosubcontrato',
            name='descripcion',
            field=models.CharField(max_length=255, blank=True, verbose_name='Descripción', help_text='Observaciones opcionales'),
        ),
    ]
