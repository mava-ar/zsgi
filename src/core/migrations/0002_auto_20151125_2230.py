# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='equipos',
            options={'verbose_name_plural': 'equipos', 'verbose_name': 'equipo'},
        ),
        migrations.AlterModelOptions(
            name='estservicio',
            options={'verbose_name_plural': 'estaciones de servicio', 'verbose_name': 'estación de servicio'},
        ),
        migrations.AlterModelOptions(
            name='francolicencia',
            options={'verbose_name_plural': 'francos y licencias', 'verbose_name': 'franco y licencia'},
        ),
        migrations.AlterModelOptions(
            name='obras',
            options={'verbose_name_plural': 'obras', 'verbose_name': 'obra'},
        ),
        migrations.AlterModelOptions(
            name='operarios',
            options={'verbose_name_plural': 'operarios', 'verbose_name': 'operario'},
        ),
        migrations.AlterModelOptions(
            name='usuario',
            options={'verbose_name_plural': 'usuarios de ZProjects', 'verbose_name': 'usuario de ZProjects'},
        ),
    ]
