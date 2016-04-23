# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documento', '0002_auto_20151125_2241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ri',
            name='fecha_creacion',
            field=models.DateField(null=True, blank=True, db_column='FECHA_CREACION'),
        ),
        migrations.AlterField(
            model_name='ri',
            name='obraid',
            field=models.ForeignKey(related_name='ris', to='core.Obras', null=True, db_column='OBRAID', blank=True),
        ),
    ]
