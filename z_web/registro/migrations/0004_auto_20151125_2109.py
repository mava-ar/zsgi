# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
        ('registro', '0003_auto_20151125_2106'),
    ]

    operations = [
        migrations.RenameField(
            model_name='combustible',
            old_name='combustibleid',
            new_name='id',
        ),
        migrations.RemoveField(
            model_name='combustible',
            name='estacionid',
        ),
        migrations.AddField(
            model_name='combustible',
            name='estacion',
            field=models.ForeignKey(related_name='consumo', to='core.EstServicio', db_column='ESTACIONID', default=1),
            preserve_default=False,
        ),
    ]
