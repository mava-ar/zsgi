# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20151126_2045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='operarios',
            name='observaciones',
            field=models.TextField(blank=True, db_column='OBSERVACIONES', null=True, max_length=255),
        ),
    ]
