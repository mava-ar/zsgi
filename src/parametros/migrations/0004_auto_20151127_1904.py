# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parametros', '0003_periodo'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='parametro',
            options={'verbose_name_plural': 'parametros del sistema', 'verbose_name': 'parametro del sistema'},
        ),
    ]
