# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0013_auto_20151220_1029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registro',
            name='dia',
            field=models.CharField(max_length=16, help_text='Indica si es sábado, domingo o otro.', choices=[('otro', 'OTRO'), ('SAB', 'SÁBADO'), ('DOM', 'Domingo')], verbose_name='Tipo de día', db_column='DIA'),
        ),
        migrations.AlterField(
            model_name='registro',
            name='especial',
            field=models.BooleanField(verbose_name='¿Se considera día especial?', db_column='ESPECIAL'),
        ),
    ]
