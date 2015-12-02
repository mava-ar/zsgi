# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documento', '0005_auto_20151125_2245'),
    ]

    operations = [
        migrations.RenameField(
            model_name='informeshoras',
            old_name='id_operario',
            new_name='operario',
        ),
    ]
