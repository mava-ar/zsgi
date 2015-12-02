# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0006_auto_20151125_2138'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partediario',
            name='desarraigo',
            field=models.BooleanField(default=False, db_column='DESARRAIGO'),
        ),
        migrations.AlterField(
            model_name='partediario',
            name='equipo',
            field=models.ForeignKey(db_column='EQUIPO', to='registro.RegistroEquipo', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='partediario',
            name='funcion',
            field=models.ForeignKey(db_column='FUNCION', to='parametros.Funcion', default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='partediario',
            name='horario',
            field=models.OneToOneField(db_column='HORARIO', to='registro.Registro', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='partediario',
            name='multifuncion',
            field=models.BooleanField(default=False, db_column='MULTIFUNCION'),
        ),
        migrations.AlterField(
            model_name='partediario',
            name='obra',
            field=models.ForeignKey(db_column='OBRA', to='core.Obras', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='partediario',
            name='operario',
            field=models.ForeignKey(to='core.Operarios', db_column='OPERARIO'),
        ),
        migrations.AlterField(
            model_name='partediario',
            name='situacion',
            field=models.ForeignKey(db_column='SITUACION', to='parametros.Situacion', default=1),
        ),
    ]
