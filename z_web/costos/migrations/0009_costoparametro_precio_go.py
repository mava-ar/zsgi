# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('costos', '0008_auto_20151201_1952'),
    ]

    operations = [
        migrations.AddField(
            model_name='costoparametro',
            name='precio_go',
            field=models.FloatField(verbose_name='Precio Gasoil', default=0, help_text='$/l a granel sin impuestos deducibles'),
            preserve_default=False,
        ),
    ]
