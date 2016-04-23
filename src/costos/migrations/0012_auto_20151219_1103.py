# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('costos', '0011_auto_20151219_1102'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='servicioprestadoun',
            unique_together=set([('periodo', 'obra')]),
        ),
    ]
