# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0004_auto_20151125_2109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registroequipo',
            name='equipo',
            field=models.ForeignKey(db_column='EQUIPO', to='core.Equipos'),
        ),
        migrations.AlterField(
            model_name='registroequipo',
            name='idservicio',
            field=models.ForeignKey(db_column='IDSERVICIO', blank=True, to='core.EstServicio', null=True),
        ),
    ]
