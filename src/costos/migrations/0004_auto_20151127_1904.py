# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('costos', '0003_auto_20151127_1608'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='costomanoobra',
            options={'verbose_name': 'costo de mano de obra', 'verbose_name_plural': 'costos de mano de obra'},
        ),
    ]
