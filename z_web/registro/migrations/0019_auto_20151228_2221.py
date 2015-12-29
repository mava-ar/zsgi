# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0018_auto_20151220_1953'),
    ]

    operations = [
        migrations.AlterField(
            model_name='certificacion',
            name='obra',
            field=models.ForeignKey(to='core.Obras', related_name='certificaciones_obras'),
        ),
        migrations.AlterField(
            model_name='certificacion',
            name='periodo',
            field=models.ForeignKey(verbose_name='Periodo', to='parametros.Periodo', related_name='certificaciones_periodo'),
        ),
    ]
