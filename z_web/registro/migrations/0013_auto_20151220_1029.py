# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0012_auto_20151220_0947'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='partediario',
            name='equipo',
        ),
        migrations.RemoveField(
            model_name='partediario',
            name='horario',
        ),
        migrations.AlterField(
            model_name='registro',
            name='partediario',
            field=models.OneToOneField(related_name='registro_horario', null=True, verbose_name='Parte Diario', to='registro.Partediario', blank=True),
        ),
        migrations.AlterField(
            model_name='registroequipo',
            name='partediario',
            field=models.OneToOneField(related_name='registro_equipo', null=True, verbose_name='Parte Diario', to='registro.Partediario', blank=True),
        ),
    ]
