# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('costos', '0004_auto_20151127_1904'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='costosubcontrato',
            name='tipo',
        ),
    ]
