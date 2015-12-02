# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documento', '0003_auto_20151125_2241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='riitem',
            name='cantidad',
            field=models.PositiveIntegerField(default=1, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='riitem',
            name='riid',
            field=models.ForeignKey(null=True, to='documento.Ri', related_name='items', db_column='riId'),
        ),
    ]
