# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0008_auto_20151125_2252'),
    ]

    operations = [
        migrations.RenameField(
            model_name='registroequipo',
            old_name='idservicio',
            new_name='estacion_servicio',
        ),
    ]
