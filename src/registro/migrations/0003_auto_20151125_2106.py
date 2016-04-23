# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0002_auto_20151125_2102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alarma',
            name='ri_id',
            field=models.ForeignKey(blank=True, null=True, db_column='RI_ID', to='documento.Ri'),
        ),
    ]
