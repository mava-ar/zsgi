# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20151126_1551'),
    ]

    operations = [
        migrations.AlterField(
            model_name='operarios',
            name='desarraigo',
            field=models.BooleanField(default=False, db_column='DESARRAIGO'),
        ),
    ]
