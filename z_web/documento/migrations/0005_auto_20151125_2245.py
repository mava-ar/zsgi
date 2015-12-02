# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documento', '0004_auto_20151125_2242'),
    ]

    operations = [
        migrations.AlterField(
            model_name='informeshoras',
            name='id_operario',
            field=models.ForeignKey(db_column='ID_OPERARIO', to='core.Operarios'),
        ),
    ]
