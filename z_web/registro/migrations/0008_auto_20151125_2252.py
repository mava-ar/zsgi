# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0007_auto_20151125_2143'),
    ]

    operations = [
        migrations.RenameField(
            model_name='materiales',
            old_name='id_registroequipo',
            new_name='registroequipo',
        ),
    ]
