# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0019_remove_materiales_registroequipo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partediario',
            name='funcion',
            field=models.ForeignKey(to='parametros.Funcion', null=True, db_column='FUNCION'),
        ),
        migrations.AlterField(
            model_name='partediario',
            name='situacion',
            field=models.ForeignKey(to='parametros.Situacion', null=True, db_column='SITUACION', default=1),
        ),
    ]
