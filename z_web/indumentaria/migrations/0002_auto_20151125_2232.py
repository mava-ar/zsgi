# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('indumentaria', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='epp',
            options={'verbose_name_plural': 'indumentaria', 'verbose_name': 'indumentaria'},
        ),
        migrations.AlterModelOptions(
            name='eppentrega',
            options={'verbose_name_plural': 'entregas de indumentaria', 'verbose_name': 'entrega de indumentaria'},
        ),
        migrations.AlterModelOptions(
            name='eppentregaitem',
            options={'verbose_name_plural': 'ítems entregas de indumentaria', 'verbose_name': 'ítem de entrega de indumentaria'},
        ),
        migrations.AlterModelOptions(
            name='eppoperarios',
            options={'verbose_name_plural': 'datos de indumentaria de operarios', 'verbose_name': 'dato de indumentario de operario'},
        ),
    ]
