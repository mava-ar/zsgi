# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0017_auto_20151220_1925'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='materiales',
            name='registroequipo',
        ),
        migrations.AlterField(
            model_name='registro',
            name='dia',
            field=models.CharField(help_text='Indica si es sábado, domingo o otro.', db_column='DIA', choices=[('otro', 'OTRO'), ('SAB', 'SÁBADO'), ('DOM', 'DOMINGO')], max_length=16, verbose_name='Tipo de día'),
        ),
        migrations.DeleteModel(
            name='Materiales',
        ),
    ]
