# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('costos', '0012_auto_20151219_1103'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='materialestotal',
            unique_together=set([('periodo', 'obra')]),
        ),
    ]
