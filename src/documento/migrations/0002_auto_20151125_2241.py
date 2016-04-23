# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documento', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='informeshoras',
            options={'verbose_name_plural': 'informes de registro horario', 'verbose_name': 'informe de registro horario'},
        ),
        migrations.AlterModelOptions(
            name='ordentrabajo',
            options={'verbose_name_plural': 'órdenes de trabajo', 'verbose_name': 'orden de trabajo'},
        ),
        migrations.AlterModelOptions(
            name='ri',
            options={'verbose_name_plural': 'requerimientos internos', 'verbose_name': 'requerimiento interno'},
        ),
        migrations.AlterModelOptions(
            name='riitem',
            options={'verbose_name_plural': 'itemes de requerimiento interno', 'verbose_name': 'item de requerimiento interno'},
        ),
    ]
