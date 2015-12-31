# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0015_auto_20151220_1216'),
    ]

    operations = [
        migrations.AlterField(
            model_name='certificacion',
            name='obra',
            field=models.ForeignKey(to='core.Obras', related_name='certificaciones_obras'),
        ),
        migrations.AlterField(
            model_name='certificacion',
            name='periodo',
            field=models.ForeignKey(related_name='certificaciones_periodo', verbose_name='Periodo', to='parametros.Periodo'),
        ),
        migrations.AlterField(
            model_name='registro',
            name='dia',
            field=models.CharField(choices=[('otro', 'OTRO'), ('SAB', 'SÁBADO'), ('DOM', 'DOMINGO')], db_column='DIA', max_length=16, help_text='Indica si es sábado, domingo o otro.', verbose_name='Tipo de día'),
        ),
    ]
